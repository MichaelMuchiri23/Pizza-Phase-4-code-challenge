from models import db

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float)

    def __init__(self, name, location, rating=None):
        self.name = name
        self.location = location
        self.rating = rating

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'rating': self.rating
        }


class Pizza(db.Model):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurantpizzas' 
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def __init__(self, restaurant_id, pizza_id):
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id