from app.models import Pago
from app.repository import PagoRepository
from app import cache

repository = PagoRepository()

class PagoService:

    def add(self, pago: Pago) -> Pago:
        result = repository.add(pago)
        if result:
            cache.set(f"pago_{result.id}", result, timeout=60)
        else:
            print("Error al añadir el pago en la base de datos")  # Mensaje de depuración
        return result

    def delete(self, id: int) -> bool:
        pago = self.find(id)
        if pago:
            cache.delete(f"pago_{id}")
            repository.delete(pago)
            return True
        else:
            print(f"Pago {id} no encontrado en la base de datos")  # Mensaje de depuración
            return False

    def find(self, id: int) -> Pago:
        return repository.find(id)