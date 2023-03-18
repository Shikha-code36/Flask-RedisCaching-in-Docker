# flask-api-with-caching
Flask Api with redis caching in docker

* **Caching Timeout** - 120s
- [Data Stored in Redis Cache](https://flaskredisapi.herokuapp.com/) 

- API that takes device ID and returns device’s latest information in response [https://127.0.0.1:5000/getdata/<device_fk_id>>](https://flaskredisapi.herokuapp.com/getdata/<device_fk_id>)
* ex- [https://127.0.0.1:5000/getdata/25029](https://127.0.0.1:5000/getdata/25029) 
- An API that takes device ID and returns start location & end location for that device. Location should be (lat, lon) tuple
[https://127.0.0.1:5000/getlocation/<device_fk_id>](https://127.0.0.1:5000/getlocation/<device_fk_id>)
* ex- [127.0.0.1:5000/getlocation/25029](127.0.0.1:5000/getlocation/25029)
- An API that takes in device ID, start time & end time and returns all the location points as list of latitude, longitude & time stamp
[127.0.0.1:5000/getinfo?deviceId=<device_fk_id>&starttime=&endtime=](127.0.0.1:5000/getinfo?deviceId=<device_fk_id>&starttime=&endtime=)
* ex- [127.0.0.1:5000/getinfo?deviceId=25029&starttime=2021-09-23T14:08:02Z&endtime=2021-10-23T14:08:02Z](127.0.0.1:5000/getinfo?deviceId=25029&starttime=2021-09-23T14:08:02Z&endtime=2021-10-23T14:08:02Z)
