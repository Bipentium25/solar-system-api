from flask import Flask
from .routes.planet_route import planet_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints here
    app.register_blueprint(planet_bp)

    return app

