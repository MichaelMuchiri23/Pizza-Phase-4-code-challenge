from flask import Flask, jsonify, request
from models import db
from models.restaurant import Restaurant
from models.pizza import Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
db.init_app(app)

# Routes for handling GET, DELETE, and POST requests
# ...

if __name__ == '__main__':
    app.run(debug=True)