# Objeto, sujeto Volcan

class Volcan:
    def __init__(self):
        self._observadores = []
        self.estado = EstadoDormido()

    def agregar_observador(self, aldeano):
        self._observadores.append(aldeano)

    def quitar_observador(self, aldeano):
        self._observadores.remove(aldeano)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def activar(self):
        self.estado.manejar(self)

    def _notificar_a_todos(self, mensaje):
        for observador in self._observadores:
            observador.alert(mensaje)

# Observers

class Aldeano:
    def __init__(self, nombre, estrategia):
        self.nombre = nombre
        self.estrategia = estrategia

    def cambiar_estrategia(self, nueva_estrategia):
        self.estrategia = nueva_estrategia

    def alert(self, mensaje):
        print(f"[{self.nombre}] ¡Alerta! {mensaje}")
        self.escapar()

    def escapar(self):
        self.estrategia.ejecutar(self.nombre)

# Strategy

class EstrategiaEscape:
    def ejecutar(self, nombre):
        raise NotImplementedError("Debes implementar el método ejecutar().")

class CorrerAlRio(EstrategiaEscape):
    def ejecutar(self, nombre):
        print(f"[{nombre}] corre hacia el río para ponerse a salvo.")

class EsconderseEnCueva(EstrategiaEscape):
    def ejecutar(self, nombre):
        print(f"[{nombre}] se esconde en una cueva cercana.")

class SalirVolando(EstrategiaEscape):
    def ejecutar(self, nombre):
        print(f"[{nombre}] se sube a un dragón y huye volando.")

# State
class EstadoVolcan:
    def manejar(self, volcan):
        raise NotImplementedError("Debes implementar el método manejar().")

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

if __name__ == "__main__":
    # Instanciar el volcán
    volcan = Volcan()

    # Crear estrategias
    rio = CorrerAlRio()
    cueva = EsconderseEnCueva()
    dragon = SalirVolando()

    Messi = Aldeano("Messi", rio)
    Pepe = Aldeano("Pepe", cueva)

    volcan.agregar_observador(Messi)
    volcan.agregar_observador(Pepe)

    volcan.activar()

    print("\n🔁 El volcán cambia a estado activo...\n")
    volcan.cambiar_estado(EstadoActivo())
    volcan.activar()

    print("\n🔁 El volcán entra en erupción...\n")
    volcan.cambiar_estado(EstadoEnErupcion())
    volcan.activar()

    print("\n🔁 [Messi cambia de estrategia a 'salir volando']\n")
    Messi.cambiar_estrategia(dragon)

    volcan.activar()
