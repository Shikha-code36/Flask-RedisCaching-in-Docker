from flask import Blueprint, jsonify, request
from models import Data
from datetime import datetime
from app import cache

locations = Blueprint('locations', __name__)

@locations.route("/getlocation/<int:device_fk_id>", methods=['GET'])
@cache.cached(timeout=120, query_string=True)
def getlocdata():
    deviceId = request.args.get('deviceId')
    start_time = datetime.strptime(
        request.args.get('starttime'), '%Y-%m-%dT%H:%M:%SZ')
    end_time = datetime.strptime(
        request.args.get('endtime'), '%Y-%m-%dT%H:%M:%SZ')
    data = Data.query.filter_by(device_fk_id=deviceId).order_by(
        Data.time_stamp.desc()).all()
    result = [{'latitude': d.latitude, 'longitude': d.longitude, 'time_stamp': d.time_stamp.strftime('%Y-%m-%dT%H:%M:%SZ')}
              for d in data if start_time <= d.time_stamp <= end_time]
    return jsonify(result)

