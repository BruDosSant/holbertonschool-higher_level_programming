class EstadoVolcan:
    def manejar(self, volcan):
        raise NotImplementedError("Debes implementar el método manejar().")
"""
Define un método común para todos los estados del volcán.
"""
class EstadoDormido(EstadoVolcan):
    def manejar(self, volcan):
        print("😴 El volcán está dormido... todo está tranquilo.")
class EstadoActivo(EstadoVolcan):
    def manejar(self, volcan):
        print("🌋 El volcán comienza a rugir y temblar... pero aún no entra en erupción.")
class EstadoEnErupcion(EstadoVolcan):
    def manejar(self, volcan):
        print("💥 ¡El volcán entra en erupción!")
        volcan._notificar_a_todos("¡El volcán está en erupción! ¡Corran!")
"""
Cada estado define su propio comportamiento al ser activado.
"""
def cambiar_estado(self, nuevo_estado):
    self.estado = nuevo_estado

def activar(self):
    self.estado.manejar(self)
"""
El volcán delegará su comportamiento actual al estado en que se encuentra.
"""
