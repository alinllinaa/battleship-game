
class Ship:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.is_sunk = False

    def check_sunk(self, hits):
        self.is_sunk = all(pos in hits for pos in self.coordinates)
