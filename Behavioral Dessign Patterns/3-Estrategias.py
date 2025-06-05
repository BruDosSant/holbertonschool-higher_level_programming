class EstrategiaEscape:
    def ejecutar(self, nombre):
        raise NotImplementedError("Debes implementar el método ejecutar().")
"""
Define una interfaz común para todas las estrategias. Cada una debe implementar ejecutar
"""
class CorrerAlRio(EstrategiaEscape):
    def ejecutar(self, nombre):
        print(f"[{nombre}] corre hacia el río para ponerse a salvo.")

class EsconderseEnCueva(EstrategiaEscape):
    def ejecutar(self, nombre):
        print(f"[{nombre}] se esconde en una cueva cercana.")

class SalirVolando(EstrategiaEscape):
    def ejecutar(self, nombre):
        print(f"[{nombre}] se sube a un dragón y huye volando.")
"""
Cada clase representa una forma distinta de escapar.

Todas implementan ejecutar(self, nombre), que recibe el nombre del aldeano.
"""
#En la clase Aldeano
def escapar(self):
    self.estrategia.ejecutar(self.nombre)
"""
El aldeano no sabe cómo escapar, solo llama a su estrategia actual.
"""
