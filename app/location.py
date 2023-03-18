from flask import Blueprint, jsonify
from models import Data
from app import cache

locations = Blueprint('locations', __name__)

@locations.route("/getlocation/<int:device_fk_id>", methods=['GET'])
@cache.cached(timeout=120, query_string=True)
def getlocdata(device_fk_id):
    data = Data.query.filter_by(device_fk_id=device_fk_id).order_by(
        Data.time_stamp.desc()).all()
    result = {}
    result["start_location"] = (data[-1].latitude, data[-1].longitude)
    result["end_location"] = (data[0].latitude, data[0].longitude)
    return jsonify(result)

