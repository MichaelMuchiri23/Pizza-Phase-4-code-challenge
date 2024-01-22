from models import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurantpizzas' 
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def __init__(self, restaurant_id, pizza_id):
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id