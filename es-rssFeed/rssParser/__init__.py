from flask import Flask


def create_app(config: str = "config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config)
    from rssParser.parser import data
    app.register_blueprint(data)
    return app