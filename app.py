from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db
from models.models import Restaurant, Pizza, RestaurantPizza
from models.seed import add_seed_data


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
db.init_app(app)

migrate = Migrate(app, db)

# Create a new restaurant
@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.json
    name = data['name']
    location = data['location']
    rating = data.get('rating') 
    new_restaurant = Restaurant(name=name, location=location, rating=rating)
    db.session.add(new_restaurant)
    db.session.commit()
    return jsonify(new_restaurant.serialize()), 201

# Get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.serialize() for restaurant in restaurants])

# Get a specific restaurant by ID
@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        return jsonify(restaurant.serialize())
    else:
        return jsonify({'message': 'Restaurant not found'}), 404

# Delete a specific restaurant by ID
@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({'message': 'Restaurant deleted successfully'})
    else:
        return jsonify({'message': 'Restaurant not found'}), 404

# Create a new pizza
@app.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.json
    name = data['name']
    price = data['price']
    new_pizza = Pizza(name=name, price=price)
    db.session.add(new_pizza)
    db.session.commit()
    return jsonify(new_pizza.serialize()), 201

# Get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.serialize() for pizza in pizzas])

# Create a new restaurant-pizza association
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    restaurant_id = data['restaurant_id']
    pizza_id = data['pizza_id']
    new_association = RestaurantPizza(restaurant_id=restaurant_id, pizza_id=pizza_id)
    db.session.add(new_association)
    db.session.commit()
    return jsonify({'message': 'Restaurant-pizza association created successfully'}), 201


if __name__ == '__main__':
    with app.app_context():
        add_seed_data()
    app.run(debug=True)