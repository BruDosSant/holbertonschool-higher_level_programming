class Aldeano:
    def __init__(self, nombre, estrategia):
        self.nombre = nombre
        self.estrategia = estrategia

"""
Crea un aldeano con un nombre y una estrategia de escape (esto es para el Strategy Pattern, lo vemos después).
"""
    def cambiar_estrategia(self, nueva_estrategia):
        self.estrategia = nueva_estrategia
"""
Permite cambiar su estrategia de escape en cualquier momento.
"""
    def alert(self, mensaje):
        print(f"[{self.nombre}] ¡Alerta! {mensaje}")
        self.escapar()
"""
Método que recibe una alerta del volcán y ejecuta la acción de escapar.
"""
    def escapar(self):
        self.estrategia.ejecutar(self.nombre)
"""
Llama a la estrategia de escape (la clase se encarga de cómo escapar).
"""
