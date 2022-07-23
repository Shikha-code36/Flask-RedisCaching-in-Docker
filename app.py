import os
from datetime import datetime
from unittest import result
from flask import Flask,request
import json
import pandas as pd
import redis
from flask_caching import Cache

# redis_host = "0.0.0.0"
# redis_port = 6500
# redis_password = ""

app=Flask(__name__)
cache=Cache(config={"CACHE_TYPE":"redis","CACHE_REDIS_HOST":"redis","CACHE_REDIS_PORT":6379,"CACHE_DEFAULT_TIMEOUT":600})
cache.init_app(app)

@app.route("/")
@cache.cached(timeout=120,query_string=True)
def set():
    df = pd.read_csv("utils/raw_data.csv")
    re = df.sort_values(
        by="sts",
        ascending=False
    )
    read=re.to_json()
    return json.loads(read)

@app.route("/getdata/<device_fk_id>", methods=['GET'])
@cache.cached(timeout=120,query_string=True)
def getdata(device_fk_id):
    df = pd.read_csv("utils/raw_data.csv")
    val =df.loc[df['device_fk_id'] == int(device_fk_id)].sort_values(by = 'time_stamp', ascending=False)
    result = json.dumps(val[:1].to_dict('records')[0])
    return json.loads(result)

@app.route("/getlocation/<device_fk_id>", methods=['GET'])
@cache.cached(timeout=120,query_string=True)
def getlocdata(device_fk_id):
    df = pd.read_csv("utils/raw_data.csv")
    val =df.loc[df['device_fk_id'] == int(device_fk_id)].sort_values(by = 'time_stamp', ascending=False)
    data = val.loc[:,['latitude','longitude']]
    response = {}
    response["start_location"] = tuple(data[:1].to_dict('records')[0].values())
    response["end_location"] = tuple(data[-1:].to_dict('records')[0].values())
    result = json.dumps(response)
    return json.loads(result)

@app.route("/getinfo", methods=['GET'])
@cache.cached(timeout=120,query_string=True)
def getfulldata():
    deviceId = request.args.get('deviceId')
    start_time = request.args.get('starttime')
    end_time = request.args.get('endtime')
    formatted_start_time = datetime.strptime(start_time,'%Y-%m-%dT%H:%M:%SZ')
    formatted_end_time = datetime.strptime(end_time,'%Y-%m-%dT%H:%M:%SZ')
    df = pd.read_csv("utils/raw_data.csv")
    val =df.loc[df['device_fk_id'] == int(deviceId)].sort_values(by = 'time_stamp', ascending=False)
    list = []
    for index,row in val.iterrows():
        item = {}
        row_time = datetime.strptime(row['time_stamp'],'%Y-%m-%dT%H:%M:%SZ')
        if row_time >= formatted_start_time and row_time <= formatted_end_time:
            item['latitude'] = row['latitude']
            item['longitude'] = row['longitude']
            item['timestamp'] = row['time_stamp']
            list.append(item)
    return json.dumps(list)    


if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port) 