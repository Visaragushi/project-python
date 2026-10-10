from flask import Blueprint, request, jsonify
from models import Reservation, Table
from db import db
from datetime import datetime, timedelta

reservations_bp = Blueprint('reservations', __name__)

@reservations_bp.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([{
        'id': r.id,
        'client_name': r.client_name,
        'table_id': r.table_id,
        'start_time': r.start_time,
        'end_time': r.end_time,
        'status': r.status
    } for r in reservations])

@reservations_bp.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.json
    reservation = Reservation(
        table_id=data['table_id'],
        client_name=data['client_name'],
        client_surname=data['client_surname'],
        email=data['email'],
        phone_number=data['phone_number'],
        start_time=datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S'),
        end_time=datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S'),
        status='confirmed'
    )
    db.session.add(reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation created successfully'}), 201
