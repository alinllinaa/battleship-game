
import pygame
import sys
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Battleship - Splash Screen")
    font = pygame.font.SysFont(None, 60)
    clock = pygame.time.Clock()

    def draw_button(text, y):
        button_rect = pygame.Rect(200, y, 200, 60)
        pygame.draw.rect(screen, (100, 100, 250), button_rect)
        txt = font.render(text, True, (255, 255, 255))
        screen.blit(txt, (button_rect.x + 25, button_rect.y + 10))
        return button_rect

    selected_difficulty = 'easy'
    start_game = False

    while not start_game:
        screen.fill((30, 30, 30))
        title = font.render("Battleship", True, (255, 255, 255))
        screen.blit(title, (180, 80))

        easy_btn = draw_button("Easy", 200)
        hard_btn = draw_button("Hard", 280)
        play_btn = draw_button("Start Game", 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_btn.collidepoint(event.pos):
                    selected_difficulty = 'easy'
                elif hard_btn.collidepoint(event.pos):
                    selected_difficulty = 'hard'
                elif play_btn.collidepoint(event.pos):
                    start_game = True

        # Show current selection
        selected_text = font.render(f"Difficulty: {selected_difficulty}", True, (255, 255, 0))
        screen.blit(selected_text, (140, 500))

        pygame.display.flip()
        clock.tick(60)

    # Start actual game
    game = Game(screen, selected_difficulty)
    game.run()

if __name__ == "__main__":
    main()
