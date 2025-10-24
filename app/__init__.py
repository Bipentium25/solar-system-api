from flask import Flask
from .db import db, migrate
from .models.planet import Planet
from .routes.planet_routes import planets_bp

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost:5432/solar_system_development'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(planets_bp)
    return app