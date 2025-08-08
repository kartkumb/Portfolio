import pygame
import sys

def select_mode():
    pygame.init()
    WIDTH, HEIGHT = 400, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Select Game Mode")

    font = pygame.font.SysFont("monospace", 32)
    small_font = pygame.font.SysFont("monospace", 24)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    RED = (200, 0, 0)

    button_yes = pygame.Rect(70, 180, 100, 50)
    button_no = pygame.Rect(230, 180, 100, 50)

    while True:
        screen.fill(BLACK)

        text = font.render("Play with AI?", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 80))

        pygame.draw.rect(screen, GREEN, button_yes)
        pygame.draw.rect(screen, RED, button_no)

        yes_text = small_font.render("Yes", True, BLACK)
        no_text = small_font.render("No", True, BLACK)

        screen.blit(yes_text, (button_yes.x + 30, button_yes.y + 10))
        screen.blit(no_text, (button_no.x + 30, button_no.y + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_yes.collidepoint(event.pos):
                    pygame.display.quit()
                    return True
                elif button_no.collidepoint(event.pos):
                    pygame.display.quit()
                    return False

def show_game_over_screen(screen, width, height, winner_text, restart_game):
    screen.fill((0, 0, 0))
    font_large = pygame.font.SysFont("monospace", 50)
    font_small = pygame.font.SysFont("monospace", 30)

    label = font_large.render(winner_text, True, (255, 255, 0))
    screen.blit(label, (width // 2 - label.get_width() // 2, height // 2 - 100))

    play_again_button = pygame.Rect(width // 2 - 150, height // 2, 140, 50)
    exit_button = pygame.Rect(width // 2 + 10, height // 2, 100, 50)

    pygame.draw.rect(screen, (0, 200, 0), play_again_button)
    pygame.draw.rect(screen, (200, 0, 0), exit_button)

    play_text = font_small.render("Play Again", True, (0, 0, 0))
    exit_text = font_small.render("Exit", True, (0, 0, 0))

    screen.blit(play_text, (play_again_button.x + 10, play_again_button.y + 10))
    screen.blit(exit_text, (exit_button.x + 20, exit_button.y + 10))

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    waiting = False
                    restart_game()
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
