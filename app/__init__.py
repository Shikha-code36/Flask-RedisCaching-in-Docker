from flask import Flask
from flask_caching import Cache
from models import db
from constant import *

cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.config['CACHE_TYPE'] = CACHE_TYPE
    app.config['CACHE_REDIS_HOST'] = CACHE_REDIS_HOST
    app.config['CACHE_REDIS_PORT'] = CACHE_REDIS_PORT
    app.config['CACHE_DEFAULT_TIMEOUT'] = CACHE_DEFAULT_TIMEOUT

    cache.init_app(app)

    from app.setData import set_bp
    from app.getData import getdata_bp
    from app.location import locations
    from app.getInfo import getinfo

    app.register_blueprint(set_bp)
    app.register_blueprint(getdata_bp)
    app.register_blueprint(locations)
    app.register_blueprint(getinfo)

    return app
