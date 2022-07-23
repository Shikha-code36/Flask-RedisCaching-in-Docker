# flask-api-with-caching
Flask Api with redis caching in docker

- [Data Stored in Redis Cache](https://flaskredisapi.herokuapp.com/) 

- API that takes device ID and returns device’s latest information in response [https://flaskredisapi.herokuapp.com/getdata/<device_fk_id>>](https://flaskredisapi.herokuapp.com/getdata/<device_fk_id>)
ex- [https://flaskredisapi.herokuapp.com/getdata/25029](https://flaskredisapi.herokuapp.com/getdata/25029) 
- An API that takes device ID and returns start location & end location for that device. Location should be (lat, lon) tuple
[https://flaskredisapi.herokuapp.com/getlocation/<device_fk_id>](https://flaskredisapi.herokuapp.com/getlocation/<device_fk_id>)
ex- [https://flaskredisapi.herokuapp.com/getlocation/25029](https://flaskredisapi.herokuapp.com/getlocation/25029)
- An API that takes in device ID, start time & end time and returns all the location points as list of latitude, longitude & time stamp
[https://flaskredisapi.herokuapp.com/getinfo?deviceId=<device_fk_id>&starttime=&endtime=](https://flaskredisapi.herokuapp.com/getinfo?deviceId=<device_fk_id>&starttime=&endtime=)
ex- [https://flaskredisapi.herokuapp.com/getinfo?deviceId=25029&starttime=2021-09-23T14:08:02Z&endtime=2021-10-23T14:08:02Z](https://flaskredisapi.herokuapp.com/getinfo?deviceId=25029&starttime=2021-09-23T14:08:02Z&endtime=2021-10-23T14:08:02Z)