from flask import Blueprint, request, jsonify
from models import Table, Restaurant
from db import db

tables_bp = Blueprint('tables', __name__)

@tables_bp.route('/restaurants/<int:restaurant_id>/tables', methods=['GET'])
def get_tables(restaurant_id):
    tables = Table.query.filter_by(restaurant_id=restaurant_id).all()
    return jsonify([{
        'id': t.id, 
        'type': t.table_type, 
        'seats': t.seat_count, 
        'price_per_hour': t.price_per_hour, 
        'smoking_allowed': t.smoking_allowed
    } for t in tables])

@tables_bp.route('/tables', methods=['POST'])
def create_table():
    data = request.json
    table = Table(
        restaurant_id=data['restaurant_id'], 
        table_type=data['table_type'], 
        seat_count=data['seat_count'], 
        price_per_hour=data['price_per_hour'], 
        smoking_allowed=data['smoking_allowed']
    )
    db.session.add(table)
    db.session.commit()
    return jsonify({'message': 'Table created successfully'}), 201
