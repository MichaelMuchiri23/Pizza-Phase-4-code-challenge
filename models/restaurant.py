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