import json
import pytest
from app import create_app
from app.models import db, Fruit

@pytest.fixture
def app():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        db.create_all()
        # Put some initial data into the database
        fruits = [
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
        ]
        db.session.bulk_save_objects(fruits)
        db.session.commit()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_getAllFruits_whenDatabaseHasFruits_returnsFruitsList(client):
    """
    Test fetching all fruits from the database
    Validates that the GET request to '/api/fruits' returns a 200 status code,
    the correct number of fruits, and specific data of the fruits
    """
    response = client.get('/api/fruits')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 2  # Adjust based on your initial data
    assert data[0]['name'] == 'Apple'

def test_addFruit_withValidData_returnsSuccessMessageAndFruitId(client):
    """
    Test adding a new fruit to the database
    Validates that the POST request to '/api/fruits' adds the fruit correctly,
    and returns a 201 status code along with a success message and the fruit's ID
    """
    new_fruit = {"name": "Orange", "quantity": 5, "variety": "Navel", "season": "Winter"}
    response = client.post('/api/fruits', json=new_fruit)
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data['message'] == 'Fruit added successfully'
    assert 'id' in data


def test_home_returnsDocumentationMessage(client):
    """
    The home route returns a 200 and a message pointing to the documentation.
    """
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'documentation' in data['message']


def test_updateFruit_withValidData_updatesFruit(client):
    """
    A PUT request to an existing fruit changes only the fields sent.
    """
    response = client.put('/api/fruits/1', json={"quantity": 99})
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'Fruit updated successfully'

    fruits = json.loads(client.get('/api/fruits').data)
    updated = [f for f in fruits if f['id'] == 1][0]
    assert updated['quantity'] == 99
    assert updated['name'] == 'Apple'  # unchanged field stays the same


def test_updateFruit_withNonexistentId_returns404(client):
    """
    A PUT request for an id that does not exist returns 404.
    """
    response = client.put('/api/fruits/999', json={"quantity": 5})
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'Fruit not found'


def test_deleteFruit_withExistingId_removesFruit(client):
    """
    A DELETE request removes the fruit, so it no longer appears in the list.
    """
    response = client.delete('/api/fruits/1')
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'Fruit deleted successfully'

    fruits = json.loads(client.get('/api/fruits').data)
    assert len(fruits) == 1
    assert all(f['id'] != 1 for f in fruits)


def test_deleteFruit_withNonexistentId_returns404(client):
    """
    A DELETE request for an id that does not exist returns 404.
    """
    response = client.delete('/api/fruits/999')
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'Fruit not found'


def test_searchFruits_byName_returnsMatchingFruits(client):
    """
    The search endpoint returns fruits matching the name query.
    """
    response = client.get('/api/fruits/search?name=Banana')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Banana'


def test_searchFruits_byMinQuantity_returnsFruitsAboveMinimum(client):
    """
    The search endpoint filters by min_quantity.
    """
    response = client.get('/api/fruits/search?min_quantity=15')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Banana'


def test_searchFruits_withNoMatches_returnsNoResultsMessage(client):
    """
    A search with no matches returns 200 and a 'no fruits found' message.
    """
    response = client.get('/api/fruits/search?name=Mango')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'No fruits found matching the search criteria'
