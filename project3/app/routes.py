from datetime import date

from flask import Blueprint, request, jsonify
from .models import db, Fruit, FruitMetrics

main = Blueprint('main', __name__)

DATE_ERROR = {'message': 'expiration_date must be in YYYY-MM-DD format'}


def parse_expiration_date(value):
    """Turn 'YYYY-MM-DD' into a date. None or '' means no expiration date.
    Raises ValueError or TypeError if the value is not a valid date string."""
    if value is None or value == '':
        return None
    return date.fromisoformat(value)


@main.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Please refer to documentation to find available endpoints'}), 200

@main.route('/api/fruits', methods=['POST'])
def add_fruit():
    data = request.json
    try:
        expiration_date = parse_expiration_date(data.get('expiration_date'))
    except (ValueError, TypeError):
        return jsonify(DATE_ERROR), 400

    fruit = Fruit(name=data['name'], quantity=data['quantity'], variety=data['variety'],
                  season=data['season'], expiration_date=expiration_date)
    db.session.add(fruit)
    db.session.commit()
    return jsonify({'message': 'Fruit added successfully', 'id': fruit.id}), 201

@main.route('/api/fruits', methods=['GET'])
def get_all_fruits():
    fruits = Fruit.query.all()
    return jsonify([fruit.serialize() for fruit in fruits]), 200

@main.route('/api/fruits/<int:fruit_id>', methods=['PUT'])
def update_fruit(fruit_id):
    data = request.json
    # Get the fruit from the DB based on id
    fruit = db.session.get(Fruit, fruit_id)
    if not fruit:
        return jsonify({'message': 'Fruit not found'}), 404

    # Validate the date first so a bad date does not leave a half-updated fruit
    new_expiration = fruit.expiration_date
    if 'expiration_date' in data:
        try:
            new_expiration = parse_expiration_date(data['expiration_date'])
        except (ValueError, TypeError):
            return jsonify(DATE_ERROR), 400

    # Updatge fruit reference in the DB with new values
    # If not present in data, leave as what is currently stored
    fruit.name = data.get('name', fruit.name)
    fruit.quantity = data.get('quantity', fruit.quantity)
    fruit.variety = data.get('variety', fruit.variety)
    fruit.season = data.get('season', fruit.season)
    fruit.expiration_date = new_expiration

    db.session.commit()
    return jsonify({'message': 'Fruit updated successfully'}), 200

@main.route('/api/fruits/<int:fruit_id>', methods=['DELETE'])
def delete_fruit(fruit_id):
    fruit = db.session.get(Fruit, fruit_id)
    if not fruit:
        return jsonify({'message': 'Fruit not found'}), 404

    db.session.delete(fruit)
    db.session.commit()
    return jsonify({'message': 'Fruit deleted successfully'}), 200

@main.route('/api/fruits/search', methods=['GET'])
def search_fruits():
    name = request.args.get('name')
    variety = request.args.get('variety')
    season = request.args.get('season')
    min_quantity = request.args.get('min_quantity', type=int)
    max_quantity = request.args.get('max_quantity', type=int)

    fruits = Fruit.search(name, variety, season, min_quantity, max_quantity)
    if not fruits:
        return jsonify({'message': 'No fruits found matching the search criteria'}), 200

    return jsonify([fruit.serialize() for fruit in fruits]), 200

@main.route('/api/fruits/expired', methods=['GET'])
def get_expired_fruits():
    fruits = Fruit.get_expired()
    return jsonify([fruit.serialize() for fruit in fruits]), 200

@main.route('/api/fruits/analytics', methods=['GET'])
def get_analytics():
    fruits = Fruit.query.all()
    return jsonify({
        'total_fruits': FruitMetrics.total_fruits(fruits),
        'total_quantity': FruitMetrics.total_quantity(fruits),
        'average_quantity': FruitMetrics.average_quantity(fruits),
        'most_common_fruit': FruitMetrics.most_common_fruit(fruits)
    }), 200
