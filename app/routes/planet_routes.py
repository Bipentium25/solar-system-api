from flask import abort, Blueprint, request, make_response
from ..models.planet import Planet
from ..db import db

planets_bp = Blueprint("planet_bp", __name__, url_prefix='/planets')

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]

    new_planet = Planet(name=name, description=description)

    db.session.add(new_planet)
    db.session.commit()

    planets_response = dict(
        id=new_planet.id,
        name=new_planet.name,
        descrtption=new_planet.description,
    )

    return planets_response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query).all()

    result_list = []

    for planet in planets:
        result_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
        ))

    return result_list
