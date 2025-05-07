from flask import Blueprint, request, Response
from ..db import db
from ..models.customer import Customer
from .route_utilties import validate_model, create_response_for_model

bp = Blueprint("customers", __name__, url_prefix="/customers")

@bp.get("")
def get_all():
    query = db.select(Customer).order_by(Customer.id)
    customers = db.session.scalars(query)
    return [customer.to_dict() for customer in customers]

@bp.get("/<id>")
def get_one(id):
    customer = validate_model(Customer, id)

    return customer.to_dict()

@bp.post("")
def create():
    return create_response_for_model(Customer, request.get_json())

@bp.put("/<id>")
def update(id):
    customer = validate_model(Customer, id)

    try:
        customer.update(request.get_json())
        
    except KeyError as error:
        response = {"details": f"Request body must include {error.args[0]}."}
        return response, 400
    
    db.session.commit()

    return Response(status=204, mimetype="application/json") # 204 No Content

@bp.delete("/<id>")
def delete(id):
    customer = validate_model(Customer, id)
    db.session.delete(customer)
    db.session.commit()
    return Response(status=204, mimetype="application/json") # 204 No Content
