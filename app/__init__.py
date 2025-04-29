from flask import Flask
import logging

from .config import get_config
from .models import db
from .routes.user_service_routes import service_api_blueprint


def create_app(config_name="development"):

    app = Flask(__name__)

    app.config.from_object(get_config(config_name))

    db.init_app(app)

    app.register_blueprint(service_api_blueprint, url_prefix='/serviceapi')

    return app

