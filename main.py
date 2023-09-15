import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants
# get height and width
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 20
FONT_COLOR = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ben's Notes App")

# Initialize font
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, 35)

running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            HEIGHT, WIDTH = event.h, event.w
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
    # Clear the screen
    screen.fill(BLACK)

    # create a loading animation of a notebook opening

    # create notepad and have boxes with titles of notes on it and make them clickable to go into notes
    # screen.blit(notepad will go here)
    # load all note names
    title_and_location = []  # Initialize title_and_location as an empty tuple
    ids = []
    notes = []
    with open("data.txt", 'r') as file:
        note_titles = []
        x = -1
        for line in file:
            x += 40
            # Process each line here
            # This will print each line without the trailing newline character
            # if there is a ((())) that means there is an assigned title; otherwise, just use the notes
            if line.strip().__contains__('((('):
                note_titles.append(line.strip().split(')))')[0][3:])
                # create id for each note
                id = ''
                for i in range(10):
                    id += str(random.randint(0, 9))
                ids.append(id)
                # HOW ID WORKS ------------------------------------- the ids are created in order so if you pull out an id from the list
                # and find its index it will be linked to the correct note since it will be on the same line
                # Append the new tuple to title_and_location
                title_and_location.append(
                    f'{x}:{id}')
            else:
                if len(line.strip()) > 20:
                    note_titles.append(line.strip()[0:15] + '...')
                    # create id for each note
                    id = ''
                    for i in range(10):
                        id += str(random.randint(0, 9))
                    ids.append(id)
                    # Append the new tuple to title_and_location
                    title_and_location.append(
                        f'{x}:{id}')
                else:
                    note_titles.append(line.strip())
                    # create id for each note
                    id = ''
                    for i in range(10):
                        id += str(random.randint(0, 9))
                    ids.append(id)
                    # Append the new tuple to title_and_location
                    title_and_location.append(
                        f'{x}:{id}')
            notes.append(line.strip())
    i = -1
    heights = []
    ids = []
    for tt in title_and_location:
        heights.append(tt.split(':')[0])
        ids.append(tt.split(':')[1])
    hovering_id = None
    # check if curser is on one of the boxes and then link it with an id
    for height in heights:
        if mouse_x >= (WIDTH // 2) - 125 and mouse_x <= (WIDTH // 2) + 80 and mouse_y >= (HEIGHT // 2) + int(height) - 205 and mouse_y <= (HEIGHT // 2) + int(height) - 175:
            height_index = heights.index(height)
            #define the id of the note your hovering over
            hovering_id = ids[height_index]
    
    if hovering_id:
        text = font.render(notes[ids.index(hovering_id)], True, WHITE)
    #make sure that your actually hovering over something
    if hovering_id != None:
        screen.blit(text, ((WIDTH // 2) - 120, (HEIGHT // 2) + i))
    for note in note_titles:
        # i is the amount of space inbetween the different note titles
        i += 40
        pygame.draw.rect(screen, (245, 245, 220), ((WIDTH // 2) - 125,
                         (HEIGHT // 2) + i - 205, 205, 30))
        screen.blit(title_font.render(note, True, BLACK),
                    ((WIDTH // 2) - 120, (HEIGHT // 2) + i - 200))

    # check if mouse is over one of the boxes

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


# # # # # # # # # # # # # # # NEXT STEP: create boxes around the titles and make it so that wehn you hover over the boxes it creates a drop down
# # # # # # # # # # # # # # # showing the title of the note and everything in it and when you take your mouse off it it close again
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
