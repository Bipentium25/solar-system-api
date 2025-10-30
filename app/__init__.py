from flask import Flask
from .db import db, migrate
from .models.planet import Planet
from .routes.planet_routes import planets_bp
import os

def create_app(config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFIplanetIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)
        
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(planets_bp)
    return app