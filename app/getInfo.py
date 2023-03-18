from flask import Blueprint, jsonify, request
from models import Data
from datetime import datetime
from app import cache

getinfo = Blueprint('getinfo', __name__)

@getinfo.route("/getinfo", methods=['GET'])
@cache.cached(timeout=120, query_string=True)
def getfulldata():
    try:
        deviceId = request.args.get('deviceId')
        start_time = request.args.get('starttime')
        end_time = request.args.get('endtime')
        formatted_start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
        formatted_end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')
        data = Data.query.filter_by(device_fk_id=deviceId).filter(
            Data.time_stamp >= formatted_start_time, Data.time_stamp <= formatted_end_time).order_by(Data.time_stamp.desc()).all()
        result = [{'latitude': d.latitude, 'longitude': d.longitude, 'time_stamp': d.time_stamp.strftime('%Y-%m-%dT%H:%M:%SZ')} for d in data]
        return jsonify(result)
    except Exception as e:
        response = {
            "errorCode": "500",
            "errorMessage": str(e)
        }
        return jsonify(response)