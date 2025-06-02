class SwimMixin:
    def swim(self):
        """Prints a message when the creature swims."""
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        """Prints a message when the creature flies."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """Prints a message when the dragon roars."""
        print("The dragon roars!")

if __name__ == "__main__":
    draco = Dragon()

    draco.swim()
    draco.fly()
    draco.roar()