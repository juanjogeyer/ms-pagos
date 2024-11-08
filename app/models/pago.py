from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Pago(db.Model):
    __tablename__ = 'pagos'

    id: int = db.Column(db.Integer, primary_key=True)
    producto: int = db.Column("producto_id", db.Integer, nullable=False)
    precio: float = db.Column(db.Float, nullable=False)
    medio_pago: str = db.Column(db.String(120), nullable=False)