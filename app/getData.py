from flask import Blueprint, jsonify
from models import Data
from app import cache

getdata_bp = Blueprint('getdata_bp', __name__)

@getdata_bp.route("/getdata/<int:device_fk_id>", methods=['GET'])
@cache.cached(timeout=120, query_string=True)
def getdata(device_fk_id):
    data = Data.query.filter_by(device_fk_id=device_fk_id).order_by(
        Data.time_stamp.desc()).first()
    result = {'device_fk_id': data.device_fk_id, 'latitude': data.latitude, 'longitude': data.longitude,
              'time_stamp': data.time_stamp.strftime('%Y-%m-%dT%H:%M:%SZ'), 'sts': data.sts, 'speed': data.speed}
    return jsonify(result)
