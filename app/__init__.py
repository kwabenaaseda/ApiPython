from flask import Flask
from flask.json import jsonify
from .routes import api
from .errors import errors

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_pyfile('config.py')
    
    # Register blueprints
    app.register_blueprint(api)
    app.register_blueprint(errors)
    
    return app