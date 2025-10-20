from flask import abort, Blueprint, make_response
from app.models.planet import planets

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")


@planet_bp.get("")
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "has_flag": planet.has_flag
            }
        )
    return planets_response

@planet_bp.get("/<id>")
def get_single_planet(id):
    # id = int(id)
    planet = validate_planet_id(id)

    return  {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "has_flag": planet.has_flag
            }
    
def validate_planet_id(id):
    try:
        id = int(id)
    except ValueError:
        invalid = {"message": f"Planet ID '{id}' is not a valid integer."}

        abort(make_response(invalid, 400))

    for planet in planets:
        if planet.id == id:
            return planet
        
    not_found = {"message": f"Planet ID '{id}' was not found."}
    abort(make_response(not_found, 404))
