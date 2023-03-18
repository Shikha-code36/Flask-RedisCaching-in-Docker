# Flask API with Redis Caching in Docker

This is a simple Flask API that uses Redis caching and can be run in a Docker container. The API has the following endpoints:

- `/getdata/<device_fk_id>`: Returns the latest information for a given device ID, including device_fk_id, latitude, longitude, time_stamp, sts, and speed.
- `/getlocation/<device_fk_id>`: Returns the start location and end location for a given device ID as a tuple of (latitude, longitude).
- `/getinfo`: Takes in device ID, start time, and end time and returns all the location points as a list of latitude, longitude, and time stamp.

The caching timeout for this API is set to 120 seconds.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run `docker-compose up --build` to start the API and Redis cache in Docker containers.
4. Use `http://127.0.0.1:5000/` as the base URL for your requests.

### Endpoints

#### /allData

Returns the latest information for all device ID, including device_fk_id, latitude, longitude, time_stamp, sts, and speed.

**Request URL:** `http://127.0.0.1:5000/allData`

**Request Method:** GET

**URL Params:**

- None

**Response:**

```
[{
"device_fk_id": "<device_fk_id>",
"latitude": "<latitude>",
"longitude": "<longitude>",
"time_stamp": "<time_stamp>",
"sts": "<sts>",
"speed": "<speed>"
},
{
"device_fk_id": "<device_fk_id>",
"latitude": "<latitude>",
"longitude": "<longitude>",
"time_stamp": "<time_stamp>",
"sts": "<sts>",
"speed": "<speed>"
}
...
]
```


#### /getdata/<device_fk_id>

Returns the latest information for a given device ID, including device_fk_id, latitude, longitude, time_stamp, sts, and speed.

**Request URL:** `http://127.0.0.1:5000/getdata/<device_fk_id>`

**Request Method:** GET

**URL Params:**

- `device_fk_id` (required): The device ID for which you want to retrieve information.

**Response:**

```
{
"device_fk_id": "<device_fk_id>",
"latitude": "<latitude>",
"longitude": "<longitude>",
"time_stamp": "<time_stamp>",
"sts": "<sts>",
"speed": "<speed>"
}
```


#### /getlocation/<device_fk_id>

Returns the start location and end location for a given device ID as a tuple of (latitude, longitude).

**Request URL:** `http://127.0.0.1:5000/getlocation/<device_fk_id>`

**Request Method:** GET

**URL Params:**

- `device_fk_id` (required): The device ID for which you want to retrieve location information.

**Response:**

```
{
"start_location": [
"<latitude>",
"<longitude>"
],
"end_location": [
"<latitude>",
"<longitude>"
]
}
```

#### /getinfo

Takes in device ID, start time, and end time and returns all the location points as a list of latitude, longitude, and time stamp.

**Request URL:** `http://127.0.0.1:5000/getinfo`

**Request Method:** GET

**URL Params:**

- `deviceId` (required): The device ID for which you want to retrieve location information.
- `starttime` (optional): The start time for the location points (format: %Y-%m-%dT%H:%M:%SZ).
- `endtime` (optional): The end time for the location points (format: %Y-%m-%dT%H:%M:%SZ).

**Response:**

```
[
{
"latitude": "<latitude>",
"longitude": "<longitude>",
"time_stamp": "<time_stamp>"
},
{
"latitude": "<latitude>",
"longitude": "<longitude>",
"time_stamp": "<time_stamp>"
},
...
]
```


## Dependencies

- Flask
- Flask-Caching
- Redis
- SQLAlchemy

## Files

```
flask-api-with-RedisCaching
├── app/
│ ├── init.py
│ ├── getData.py
│ ├── getInfo.py
│ ├── location.py
│ └── setData.py
├── utils/
│ └── raw_data.csv
├── .gitignore
├── data.py
├── constant.py
├── Dockerfile
├── docker-compose.yml
└── model.py
```

- `app/`: Contains the Flask application code.
    - `__init__.py`: Initializes the Flask app and registers the routes.
    - `getData.py`: Contains the code for the `/getdata/<device_fk_id>` endpoint.
    - `getInfo.py`: Contains the code for the `/getinfo` endpoint.
    - `location.py`: Contains the code for the `/getlocation/<device_fk_id>` endpoint.
    - `setData.py`: Contains the code for the `/setdata` endpoint.
- `utils/`: Contains the raw data in `raw_data.csv` file.
- `.gitignore`: Specifies files that should be ignored by Git.
- `data.py`: Contains functions for retrieving data.
- `constant.py`: Contains constant values used throughout the application.
- `Dockerfile`: Contains instructions for building the Docker image.
- `docker-compose.yml`: Contains instructions for running the Docker container.
- `model.py`: Contains the data model for the application.

## Caching

The application uses Redis as the caching layer, with a caching timeout of 120 seconds.