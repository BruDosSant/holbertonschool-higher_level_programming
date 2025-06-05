class Volcan:
    def __init__(self):
        self._observadores = []
        self.estado = EstadoDormido()
"""
Crea una lista vacía de observadores (aldeanos) y empieza en estado dormido.
"""
    def agregar_observador(self, aldeano):
        self._observadores.append(aldeano)

    def quitar_observador(self, aldeano):
        self._observadores.remove(aldeano)
"""
Métodos para añadir o quitar aldeanos que observan al volcán
"""
    def _notificar_a_todos(self, mensaje):
        for observador in self._observadores:
            observador.alert(mensaje)
"""
El corazón del patrón Observer: el volcán avisa a todos los aldeanos registrados enviando el mensaje.
"""
