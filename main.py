import pygame
import sys
import json
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 20
FONT_COLOR = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ultimate Notes")

# Initialize font
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, 35)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            HEIGHT, WIDTH = event.h, event.w
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
    # Clear the screen
    screen.fill((50, 50, 170))

    # create a loading animation of a notebook opening

    # create notepad and have boxes with titles of notes on it and make them clickable to go into notes
    # screen.blit(notepad will go here)
    # load all note names
    with open("Ultimate-Notes-App\data.txt", 'r') as file:
        note_titles = []
        for line in file:
            # Process each line here
            # This will print each line without the trailing newline character
            if len(line.strip()) > 20:
                note_titles.append(line.strip()[0:20] + '...')
            else:
                note_titles.append(line.strip())

        # print(note_titles)
    i = -1
    for note in note_titles:
        # i is the amount of space inbetween the different note titles
        i += 40
        screen.blit(title_font.render(note, True, WHITE),
                    ((WIDTH // 2) - 120, (HEIGHT // 2) + i - 200))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


# # # # # # # # # # # # # # # NEXT STEP: create boxes around the titles and make it so that wehn you hover over the boxes it creates a drop down
# # # # # # # # # # # # # # # showing the title of the note and everything in it and when you take your mouse off it it close again
# # # # # # # # # # # # # # # NEXT STEP: make it so that the title would only be the first 20 letters if theres no title which can be defined in the
# # # # # # # # # # # # # # # data.txt file with (((title here))) you can use .split() to seperate the title and the text
