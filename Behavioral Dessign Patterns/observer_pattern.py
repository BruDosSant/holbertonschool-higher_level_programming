# observer_pattern.py

class Aldeano:
    def __init__(self, name):
        self.name = name

    def alert(self, mensaje):
        print(f"[{self.name}] ¡Alerta! {mensaje}")


class Volcan:
    def __init__(self):
        self._observers = []
        self._erupcion = False

    def add_observer(self, aldeano):
        self._observers.append(aldeano)

    def remove_observer(self, aldeano):
        self._observers.remove(aldeano)

    def erupt(self):
        self._erupcion = True
        print("\n🌋 El volcán comienza a temblar...")
        self._notify_all("¡El volcán está en erupción! ¡Corran!")

    def _notify_all(self, mensaje):
        for observer in self._observers:
            observer.alert(mensaje)
