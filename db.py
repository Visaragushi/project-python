from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from enum import Enum as PyEnum

db = SQLAlchemy()
migrate = Migrate()

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class TableType(PyEnum):
    vip = 'vip'
    client = 'client'
    meeting = 'meeting'

class Table(db.Model):
    __tablename__ = 'table'
    
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    table_type = db.Column(db.Enum(TableType), nullable=False)
    seat_count = db.Column(db.Integer, nullable=False)
    price_per_hour = db.Column(db.Float, nullable=False)
    smoking_allowed = db.Column(db.Boolean, default=False)
    
    restaurant = db.relationship('Restaurant', backref='tables')

class ReservationStatus(PyEnum):
    confirmed = 'confirmed'
    cancelled = 'cancelled'
    checked_in = 'checked-in'

class Reservation(db.Model):
    __tablename__ = 'reservation'
    
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)
    client_name = db.Column(db.String(50), nullable=False)
    client_surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(ReservationStatus), default=ReservationStatus.confirmed)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    table = db.relationship('Table', backref='reservations')

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:visar123@localhost/restaurant_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

# Flask app initialization (example)
# app = Flask(__name__)
# init_db(app)
