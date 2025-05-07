
import pygame
from board import Board

CELL_SIZE = 40
GRID_SIZE = 10
MARGIN = 50

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)
        self.board_p1 = Board()
        self.board_p2 = Board()
        self.current_player = 1
        self.phase = "setup"
        self.message = "Player 1: Place your ships"

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.fill((0, 0, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    grid_x = (x - MARGIN) // CELL_SIZE
                    grid_y = (y - MARGIN) // CELL_SIZE
                    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
                        self.handle_click(grid_x, grid_y)

            self.draw_board()
            pygame.display.flip()
            clock.tick(30)

    def handle_click(self, x, y):
        if self.phase == "setup":
            if self.current_player == 1:
                self.board_p1.place_ship(x, y)
                if self.board_p1.all_ships_placed():
                    self.current_player = 2
                    self.message = "Player 2: Place your ships"
            elif self.current_player == 2:
                self.board_p2.place_ship(x, y)
                if self.board_p2.all_ships_placed():
                    self.phase = "battle"
                    self.current_player = 1
                    self.message = "Player 1: Your turn"
        elif self.phase == "battle":
            target_board = self.board_p2 if self.current_player == 1 else self.board_p1
            target_board.attack(x, y)
            self.current_player = 2 if self.current_player == 1 else 1
            self.message = f"Player {self.current_player}: Your turn"

    def draw_board(self):
        self.screen.blit(self.font.render(self.message, True, (255, 255, 255)), (50, 10))
        offset_x = MARGIN
        offset_y = MARGIN

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(offset_x + x * CELL_SIZE, offset_y + y * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2)
                pygame.draw.rect(self.screen, (0, 100, 200), rect, 1)
