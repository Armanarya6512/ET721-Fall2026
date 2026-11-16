import pytest
from app import create_app
from app.models import Fruit, FruitMetrics, db


@pytest.fixture(scope='module')
def test_app():
    # Setup: create a Flask app instance
    app = create_app()
    # Push an application context
    ctx = app.app_context()
    ctx.push()

    # Setup the database
    with app.app_context():
        db.create_all()

        # Add fruits to the database once for all search tests
        fruits = [
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
            Fruit(name="Apple", quantity=15, variety="Fuji", season="Winter"),
        ]
        db.session.bulk_save_objects(fruits)
        db.session.commit()

    yield app  # this is where the testing happens

    # Teardown: remove the application context
    ctx.pop()


def test_searchByName_withExistingFruitName_returnsFruitsWithName(test_app):
    """
    Search by name returns only the fruits whose name matches.
    """
    with test_app.app_context():
        results = Fruit.search(name="Apple")
        assert len(results) == 2
        assert all(fruit.name == "Apple" for fruit in results)


def test_searchByVariety_withExistingVariety_returnsMatchingFruit(test_app):
    """
    Search by variety returns the fruit with that variety.
    """
    with test_app.app_context():
        results = Fruit.search(variety="Cavendish")
        assert len(results) == 1
        assert results[0].name == "Banana"


def test_searchBySeason_withExistingSeason_returnsMatchingFruits(test_app):
    """
    Search by season returns every fruit in that season.
    """
    with test_app.app_context():
        results = Fruit.search(season="Winter")
        assert len(results) == 2


def test_searchByMinQuantity_withMinimum_returnsFruitsAtOrAboveMinimum(test_app):
    """
    Search by min_quantity only returns fruits with quantity >= the minimum.
    """
    with test_app.app_context():
        results = Fruit.search(min_quantity=15)
        assert len(results) == 2
        assert all(fruit.quantity >= 15 for fruit in results)


def test_searchByMaxQuantity_withMaximum_returnsFruitsAtOrBelowMaximum(test_app):
    """
    Search by max_quantity only returns fruits with quantity <= the maximum.
    """
    with test_app.app_context():
        results = Fruit.search(max_quantity=15)
        assert len(results) == 2
        assert all(fruit.quantity <= 15 for fruit in results)


def test_search_withNoMatches_returnsEmptyList(test_app):
    """
    Search with criteria that match nothing returns an empty list.
    """
    with test_app.app_context():
        assert Fruit.search(name="Mango") == []


def test_search_withMultipleCriteria_returnsOnlyFruitsMatchingAll(test_app):
    """
    Combining filters narrows the results to fruits matching every filter.
    """
    with test_app.app_context():
        results = Fruit.search(name="Apple", min_quantity=15)
        assert len(results) == 1
        assert results[0].variety == "Fuji"


def test_serialize_withFruit_returnsDictionaryOfAttributes():
    """
    serialize() turns a Fruit into a dictionary with all its attributes.
    """
    fruit = Fruit(name="Apple", quantity=10, variety="Gala", season="Winter")
    assert fruit.serialize() == {
        'id': None,
        'name': 'Apple',
        'quantity': 10,
        'variety': 'Gala',
        'season': 'Winter',
        'expiration_date': None,
    }


def test_createFruit_withShortName_raisesAssertionError():
    """
    Names with 2 characters or fewer are rejected.
    """
    with pytest.raises(AssertionError):
        Fruit(name="Ab", quantity=10)


def test_averageQuantity_withEmptyList_returnsZero():
    """
    The average of an empty inventory is 0 (not a crash).
    """
    assert FruitMetrics.average_quantity([]) == 0


def test_mostCommonFruit_withEmptyList_returnsNone():
    """
    With no fruits there is no most common fruit.
    """
    assert FruitMetrics.most_common_fruit([]) is None
