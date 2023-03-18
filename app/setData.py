from flask import Blueprint, jsonify
from models import db, Data
from data import *
from app import cache

set_bp = Blueprint('set_bp', __name__)

@set_bp.before_app_first_request
def create_tables():
    db.create_all()
    populate_database_from_csv()

@set_bp.route('/allData', methods=['GET'])
@cache.cached(timeout=120, query_string=True)
def set():
    data = Data.query.order_by(Data.sts.desc()).all()
    result = [{'device_fk_id': d.device_fk_id, 'latitude': d.latitude, 'longitude': d.longitude,
               'time_stamp': d.time_stamp.strftime('%Y-%m-%dT%H:%M:%SZ'), 'sts': d.sts, 'speed': d.speed} for d in data]
    return jsonify(result)
