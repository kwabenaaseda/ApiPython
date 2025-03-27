from flask import Blueprint, jsonify, request
import os

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return jsonify({"message": "Hello World",
                    "status": "success"})

@api.route('/<path:subpath>')
def dynamic_route(subpath):
    return jsonify({
        "message": f"You requested: /{subpath}",
        "method": request.method,
        "success": True
    })

@api.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "environment": os.getenv('FLASK_ENV', 'development')
    })