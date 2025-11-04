from flask import abort, Blueprint, make_response, request
from ..routes.routes_utilities import validate_model, create_model, get_models_with_filters
from ..models.planet import Planet
from ..models.moon import Moon
from ..db import db

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()

    return create_model(Planet, request_body)

@bp.post("/<id>/moons")
def create_moon_with_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()
    request_body["planet_id"] = planet.id
    return create_model(Moon, request_body)

@bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)

@bp.get("/<id>/moons")
def get_all_planet_moons(id):
    planet = validate_model(Planet, id)

    moons = [moon.to_dict() for moon in planet.moons]

    return moons