
class Cell:
    def __init__(self):
        self.has_ship = False
        self.is_hit = False

    def place_ship(self):
        self.has_ship = True

    def attack(self):
        self.is_hit = True
        return self.has_ship
