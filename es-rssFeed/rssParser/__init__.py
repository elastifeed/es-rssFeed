from flask import Flask
from config import DevelopmentConfig


def create_app(this):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    from rssParser.parser import data
    app.register_blueprint(data)
    return app