from flask import Blueprint, request
from marshmallow import ValidationError
from .services import PagoService, ResponseBuilder
from .mapping import PagoSchema, ResponseSchema

pago = Blueprint('pago', __name__)

pago_service = PagoService()
pago_schema = PagoSchema()
response_schema = ResponseSchema()

@pago.route('/pagos/add', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    try:
        pago = pago_schema.load(request.json)
        data = pago_schema.dump(pago_service.add(pago))
        response_builder.add_message("Pago added").add_status_code(201).add_data(data)
        return response_schema.dump(response_builder.build()), 201
    except ValidationError as err:
        response_builder.add_message("Validation error").add_status_code(422).add_data(err.messages)
        return response_schema.dump(response_builder.build()), 422

@pago.route('/pagos/cancelar/<int:id>', methods=['DELETE'])
def cancelar_pago(id):
    response_builder = ResponseBuilder()
    data = pago_service.delete(id)
    if data:
        response_builder.add_message("Pago deleted").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Pago not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404