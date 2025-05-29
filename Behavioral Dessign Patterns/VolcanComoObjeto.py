"""Tiene una lista de observadores (_observers)"""

self._observers = []

"""Tiene métodos para agregar o quitar observadores"""

def add_observer(self, villager):
    self._observers.append(villager)

"""Cuando algo importante pasa (la erupción), notifica a todos los observadores"""

def _notify_all(self, message):
    for observer in self._observers:
        observer.alert(message)

