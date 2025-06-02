class Fish:
    """
    Fish class with methods related to swimming and habitat.
    """
    
    def swim(self):
        """Simulates the fish swimming."""
        print("The fish is swimming")
    
    def habitat(self):
        """Returns the habitat of the fish."""
        print("The fish lives in water")

class Bird:
    """
    Bird class with methods related to flying and habitat.
    """
    
    def fly(self):
        """Simulates the bird flying."""
        print("The bird is flying")
    
    def habitat(self):
        """Returns the habitat of the bird."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird.
    """
    
    def swim(self):
        """Overrides the swim method."""
        print("The flying fish is swimming!")
    
    def fly(self):
        """Overrides the fly method."""
        print("The flying fish is soaring!")
    
    def habitat(self):
        """Overrides the habitat method."""
        print("The flying fish lives both in water and the sky!")
