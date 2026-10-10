from flask import Blueprint, request, jsonify # type: ignore
from models import Restaurant
from db import db

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'location': r.location} for r in restaurants])

@restaurants_bp.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.json
    restaurant = Restaurant(name=data['name'], location=data['location'], description=data['description'])
    db.session.add(restaurant)
    db.session.commit()
    return jsonify({'message': 'Restaurant created successfully'}), 201
