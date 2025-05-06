
import pygame
import time

class Game:
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.difficulty = difficulty
        self.running = True
        self.turn_time = 10 if difficulty == "hard" else None
        self.font = pygame.font.SysFont(None, 36)

    def run(self):
        clock = pygame.time.Clock()
        start_time = time.time()

        while self.running:
            self.screen.fill((0, 0, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Simple placeholder grid
            for y in range(10):
                for x in range(10):
                    pygame.draw.rect(self.screen, (0, 100, 200), (50 + x*40, 50 + y*40, 38, 38), 1)

            # Timer
            if self.difficulty == "hard":
                elapsed = int(time.time() - start_time)
                remaining = max(0, self.turn_time - elapsed)
                timer_text = self.font.render(f"Time left: {remaining}", True, (255, 255, 255))
                self.screen.blit(timer_text, (400, 10))
                if remaining <= 0:
                    print("Turn over!")
                    start_time = time.time()

            pygame.display.flip()
            clock.tick(30)
