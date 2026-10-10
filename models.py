from db import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    table_type = db.Column(db.Enum('vip', 'client', 'meeting'), nullable=False)
    seat_count = db.Column(db.Integer, nullable=False)
    price_per_hour = db.Column(db.Float, nullable=False)
    smoking_allowed = db.Column(db.Boolean, default=False)
    restaurant = db.relationship('Restaurant', backref='tables')

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)
    client_name = db.Column(db.String(50), nullable=False)
    client_surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum('confirmed', 'cancelled', 'checked-in'), default='confirmed')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    table = db.relationship('Table', backref='reservations')
