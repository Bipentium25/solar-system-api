from flask import abort, Blueprint, request, make_response, Response
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
    query = db.select(Planet)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name == name_param)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
        
    query = query.order_by(Planet.id)

    planets = db.session.scalars(query).all()

    result_list = []

    for planet in planets:
        result_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
        ))

    return result_list

@planets_bp.get("/<id>")
def get_single_planets(id):
    # query = db.select(planet).where(planet.id == id)
    # planet = db.session.scalar(query)
    planet = validate_planet(id)
    planet_dict = dict(
        id=planet.id,
        name=planet.name,
        description=planet.description
    )

    return planet_dict

def validate_planet(id):
    try:
        id = int(id)
    except ValueError:

        abort(make_response({"message": f"planet {id} invalid"}, 400))

    query = db.select(Planet).where(Planet.id == id)
    planet = db.session.scalar(query)

    if not planet:
        abort(make_response({"message": f"planet {id} not found"}, 404))

    return planet
        
@planets_bp.put("/<id>")
def replace_planet(id):
    planet = validate_planet(id)

    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()

    return Response(status=204, mimetype="appliplanetion/json")

@planets_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="appliplanetion/json")
