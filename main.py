import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 24
FONT_COLOR = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ultimate Notes")

# Initialize font
font = pygame.font.Font(None, FONT_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
    # Clear the screen
    screen.fill(BLACK)

    # create notepad and have boxes with titles of notes on it and make them clickable to go into notes
    # screen.blit()
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
