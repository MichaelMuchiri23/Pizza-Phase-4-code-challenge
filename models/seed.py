from .models import db, Restaurant, Pizza

def add_seed_data():
    # Add seed data for restaurants
    restaurant1 = Restaurant(name='Pizzeria Uno', location='New York', rating=4.5)
    restaurant2 = Restaurant(name='Pizza Hut', location='Chicago', rating=4.0)
    db.session.add(restaurant1)
    db.session.add(restaurant2)

    # Add seed data for pizzas
    pizza1 = Pizza(name='Margherita', price=12.99)
    pizza2 = Pizza(name='Pepperoni', price=14.99)
    db.session.add(pizza1)
    db.session.add(pizza2)

    db.session.commit()