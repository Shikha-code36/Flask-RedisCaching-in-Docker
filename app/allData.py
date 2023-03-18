from flask import Blueprint, jsonify
from models import db, Data
from data import *
from app import cache

data_bp = Blueprint('data_bp', __name__)

@data_bp.before_app_first_request
def create_tables():
    db.create_all()
    populate_database_from_csv()

@data_bp.route('/alldata', methods=['GET'])
@cache.cached(timeout=120, query_string=True)
def retrive_data():
    data = Data.query.order_by(Data.sts.desc()).all()
    result = [{'device_fk_id': d.device_fk_id, 'latitude': d.latitude, 'longitude': d.longitude,
               'time_stamp': d.time_stamp.strftime('%Y-%m-%dT%H:%M:%SZ'), 'sts': d.sts, 'speed': d.speed} for d in data]
    return jsonify(result)
