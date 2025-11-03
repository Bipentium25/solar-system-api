from flask import abort, make_response
from ..db import db

def validate_model(cls, id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response({"message": f"{cls.__name__} id {id} invalid"}, 400))

    query = db.select(cls).where(cls.id == id)
    model = db.session.scalar(query)

    if not model:
        abort(make_response({"message": f"{cls.__name__} with id {id} not found"}, 404))

    return model