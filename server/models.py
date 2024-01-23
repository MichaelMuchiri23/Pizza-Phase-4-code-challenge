from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float)
    restaurant = db.relationship('RestaurantPizza', backref='restaurants')


    def __init__(self, name, address, rating=None):
        self.name = name
        self.address = address
        self.rating = rating

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'rating': self.rating
        }


class Pizza(db.Model):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(100), nullable=False)
    pizza = db.relationship('RestaurantPizza', backref='pizzas')


    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
       

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas' 
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable = False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    
   

    def __init__(self, restaurant_id, pizza_id, price):
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id
        self.price = price


       