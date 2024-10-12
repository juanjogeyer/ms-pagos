from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config
import os

db = SQLAlchemy()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    app = Flask(__name__)
    #app.config.from_object('app.config.Config')
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)
    
    db.init_app(app)

    with app.app_context():
        from app.resource import pago
        app.register_blueprint(pago)

    return app