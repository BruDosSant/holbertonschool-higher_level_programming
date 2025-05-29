# main.py

from observer_pattern import Volcan, Aldeano

def run_observer_game():
    print("🛰️ Misión 1: El volcán dormido")

    volcan = Volcan()

    # Crear aldeanos
    Messi = Aldeano("Messi")
    Pepe = Aldeano("Pepe")
    Jose = Aldeano("Jose")

    # Los aldeanos se suscriben al volcán
    volcan.add_observer(Messi)
    volcan.add_observer(Pepe)
    volcan.add_observer(Jose)

    input("\nPresioná ENTER para continuar...")

    print("\n☁️ Todo parece tranquilo en la aldea... por ahora.")
    input("\nPresioná ENTER para simular la erupción...")

    # Simular erupción
    volcan.erupt()

if __name__ == "__main__":
    run_observer_game()
