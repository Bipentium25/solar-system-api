from flask import Blueprint, request, Response
from ..models.planet import Planet
from ..db import db
from ..routes.routes_utilities import validate_model

planets_bp = Blueprint("planet_bp", __name__, url_prefix='/planets')

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    # name = request_body["name"]
    # description = request_body["description"]

    try:
        new_planet = Planet.from_dict(request_body)
    except KeyError as error:
        return {"error": f"Missing required field: {error.args[0]}"}, 400

    db.session.add(new_planet)
    db.session.commit()

    # planets_response = dict(
    #     id=new_planet.id,
    #     name=new_planet.name,
    #     description=new_planet.description,
    # )

    return new_planet.to_dict(), 201



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
        result_list.append(planet.to_dict())

    return result_list

@planets_bp.get("/<id>")
def get_single_planets(id):
    # query = db.select(planet).where(planet.id == id)
    # planet = db.session.scalar(query)
    planet = validate_model(Planet, id)
    # planet_dict = dict(
    #     id=planet.id,
    #     name=planet.name,
    #     description=planet.description
    # )

    return planet.to_dict()

        
@planets_bp.put("/<id>")
def replace_planet(id):
    planet = validate_model(Planet, id)

    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()

    return Response(status=204, mimetype="appliplanetion/json")

@planets_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_model(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="appliplanetion/json")
