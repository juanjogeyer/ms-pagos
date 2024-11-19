from app.models import Pago
from app.repository import PagoRepository
from app import cache

repository = PagoRepository()

class PagoService:

    def add(self, pago: Pago) -> Pago:
        result = repository.add(pago)
        if result:
            cache.set(f"pago_{result.id}", result, timeout=60)
            print(f"Pago {result.id} añadido al caché")  # Mensaje de depuración
        else:
            print("Error al añadir el pago en la base de datos")  # Mensaje de depuración
        return result

    def delete(self, id: int) -> bool:
        pago = self.find(id)
        if pago:
            cache.delete(f"pago_{id}")
            print(f"Pago {id} eliminado del caché")  # Mensaje de depuración
            repository.delete(pago)
            print(f"Pago {id} eliminado de la base de datos")  # Mensaje de depuración
            return True
        else:
            print(f"Pago {id} no encontrado en la base de datos")  # Mensaje de depuración
            return False

    def find(self, id: int) -> Pago:
        return repository.find(id)