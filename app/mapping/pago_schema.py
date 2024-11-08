from marshmallow import Schema, fields, post_load
from app.models.pago import Pago

class PagoSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto = fields.Integer(required=True)
    precio = fields.Float(required=True)
    medio_pago = fields.String(required=True)

    @post_load
    def make_pago(self, data, **kwargs):
        return Pago(**data)