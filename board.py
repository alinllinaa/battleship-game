
from cell import Cell

class Board:
    def __init__(self):
        self.grid = [[Cell() for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.max_ships = 5

    def place_ship(self, x, y):
        if len(self.ships) < self.max_ships:
            self.grid[y][x].place_ship()
            self.ships.append((x, y))

    def all_ships_placed(self):
        return len(self.ships) == self.max_ships

    def attack(self, x, y):
        self.grid[y][x].attack()
