
import pygame
import time
import os

CELL_SIZE = 40
GRID_SIZE = 10
MARGIN = 50

class Game:
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.difficulty = difficulty
        self.running = True
        self.font = pygame.font.SysFont(None, 36)
        self.turn_time = 10 if difficulty == "hard" else None
        self.placed_ships = []
        self.max_ships = 5
        self.placing_ships = True
        self.attacked_cells = {}
        self.hit_sound = pygame.mixer.Sound(os.path.join("assets", "hit.wav"))
        self.miss_sound = pygame.mixer.Sound(os.path.join("assets", "miss.wav"))

    def run(self):
        clock = pygame.time.Clock()
        start_time = time.time()

        while self.running:
            self.screen.fill((0, 0, 50))
            mouse_clicked = False
            mouse_pos = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True
                    mouse_pos = event.pos

            # Draw grid
            for y in range(GRID_SIZE):
                for x in range(GRID_SIZE):
                    rect = pygame.Rect(MARGIN + x*CELL_SIZE, MARGIN + y*CELL_SIZE, CELL_SIZE-2, CELL_SIZE-2)
                    color = (0, 100, 200)
                    if (x, y) in self.placed_ships:
                        color = (0, 255, 0)
                    if (x, y) in self.attacked_cells:
                        color = (255, 0, 0) if self.attacked_cells[(x, y)] else (100, 100, 100)
                    pygame.draw.rect(self.screen, color, rect)

            # Ship placement
            if self.placing_ships and mouse_clicked:
                grid_x = (mouse_pos[0] - MARGIN) // CELL_SIZE
                grid_y = (mouse_pos[1] - MARGIN) // CELL_SIZE
                if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
                    if len(self.placed_ships) < self.max_ships and (grid_x, grid_y) not in self.placed_ships:
                        self.placed_ships.append((grid_x, grid_y))
                    if len(self.placed_ships) == self.max_ships:
                        self.placing_ships = False
                        print("Ships placed:", self.placed_ships)

            # Attack phase
            elif not self.placing_ships and mouse_clicked:
                grid_x = (mouse_pos[0] - MARGIN) // CELL_SIZE
                grid_y = (mouse_pos[1] - MARGIN) // CELL_SIZE
                if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
                    if (grid_x, grid_y) not in self.attacked_cells:
                        hit = (grid_x, grid_y) in self.placed_ships
                        self.attacked_cells[(grid_x, grid_y)] = hit
                        if hit:
                            self.hit_sound.play()
                        else:
                            self.miss_sound.play()

            # Timer
            if self.difficulty == "hard" and not self.placing_ships:
                elapsed = int(time.time() - start_time)
                remaining = max(0, self.turn_time - elapsed)
                timer_text = self.font.render(f"Time left: {remaining}", True, (255, 255, 255))
                self.screen.blit(timer_text, (400, 10))
                if remaining <= 0:
                    print("Turn over!")
                    start_time = time.time()

            # Instructions
            if self.placing_ships:
                text = self.font.render(f"Place your ships ({len(self.placed_ships)}/{self.max_ships})", True, (255, 255, 0))
            else:
                text = self.font.render("Click to attack!", True, (0, 255, 255))
            self.screen.blit(text, (50, 10))

            # Check win
            if not self.placing_ships:
                all_sunk = all(cell in self.attacked_cells and self.attacked_cells[cell] for cell in self.placed_ships)
                if all_sunk:
                    win_text = self.font.render("All ships sunk! You win!", True, (255, 255, 0))
                    self.screen.blit(win_text, (150, 550))

            pygame.display.flip()
            clock.tick(30)
