from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app 
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

def add_seed_data():
    # Add seed data for restaurants
    restaurant1 = Restaurant(name='Pizzeria Uno', address='New York', rating=4.5)
    restaurant2 = Restaurant(name='Pizza Hut', address='Chicago', rating=4.0)
    db.session.add(restaurant1)
    db.session.add(restaurant2)

    db.session.commit()

    # Add seed data for pizzas
    pizza1 = Pizza(name='Margherita', ingredients= "Cheese, Tomatoes, Basil")
    pizza2 = Pizza(name='Pepperoni', ingredients= "Cheese, Pepperoni, Tomatoes")
    db.session.add(pizza1)
    db.session.add(pizza2)

    db.session.commit()

    # Add seed data for restaurant_pizzas
    restaurant_pizzas1 = RestaurantPizza(price=5, restaurant_id=1, pizza_id=1)
    restaurant_pizzas2 = RestaurantPizza(price=7, restaurant_id=2, pizza_id=2)
    db.session.add(restaurant_pizzas1)
    db.session.add(restaurant_pizzas2)

    db.session.commit()
