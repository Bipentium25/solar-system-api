from flask import Blueprint, request, Response
from ..models.moon import Moon
from ..db import db
from ..routes.routes_utilities import validate_model, create_model, get_models_with_filters

bp = Blueprint("moon_bp", __name__, url_prefix='/moons')

@bp.post("")
def create_moon():
    request_body = request.get_json()

    return create_model(Moon, request_body)

@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moon, request.args)

@bp.get("/<id>")
def get_single_moons(id):

    moon = validate_model(Moon, id)
    return moon.to_dict()
        
@bp.put("/<id>")
def replace_moon(id):
    moon = validate_model(Moon, id)

    request_body = request.get_json()
    moon.name = request_body["name"]
    moon.size = request_body["size"]
    moon.description = request_body["description"]
    moon.has_flag = request_body["has_flag"]

    db.session.commit()

    return Response(status=204, mimetype="applimoonion/json")

@bp.delete("/<id>")
def delete_moon(id):
    moon = validate_model(Moon, id)

    db.session.delete(moon)
    db.session.commit()

    return Response(status=204, mimetype="applimoonion/json")