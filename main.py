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
FONT_COLOR = (255, 255, 255)
open_frame = 0
open_height = 0

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ben's Notes App")

# Initialize font
font = pygame.font.Font('Ultimate-Notes-App\Oswald-Medium.ttf', 22)
title_font = pygame.font.Font('Ultimate-Notes-App\Oswald-Medium.ttf', 27)

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
    with open("Ultimate-Notes-App\data.txt", 'r') as file:
        note_titles = []
        x = -1
        for line in file:
            x += 40
            # Process each line here
            # This will print each line without the trailing newline character
            # if there is a ((())) that means there is an assigned title; otherwise, just use the notes
            if line.strip().__contains__('((('):
                if len(line.strip().split(')))')[0][3:]) < 20:
                    note_titles.append(line.strip().split(')))')[0][3:])
                else:
                    note_titles.append(line.strip().split(')))')[
                                       0][3:17] + '...')
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
                    note_titles.append(line.strip()[0:17] + '...')
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
    for note in note_titles:
        # i is the amount of space inbetween the different note titles
        i += 40
        # create boxes around the note names
        pygame.draw.rect(screen, (255, 240, 200), ((WIDTH // 2) - 125,
                         (HEIGHT // 2) + i - 205, 205, 30))
        screen.blit(title_font.render(note, True, BLACK),
                    ((WIDTH // 2) - 120, (HEIGHT // 2) + i - 210))
    for tt in title_and_location:
        heights.append(tt.split(':')[0])
        ids.append(tt.split(':')[1])
    hovering_id = None
    # check if curser is on one of the boxes and then link it with an id
    for height in heights:
        if mouse_x >= (WIDTH // 2) - 125 and mouse_x <= (WIDTH // 2) + 80 and mouse_y >= (HEIGHT // 2) + int(height) - 205 and mouse_y <= (HEIGHT // 2) + int(height) - 175:
            height_index = heights.index(height)
            # define the id of the note your hovering over
            hovering_id = ids[height_index]
            pygame.draw.rect(screen, (WHITE), ((WIDTH // 2) - 125,
                                               (HEIGHT // 2) + int(height) - 205, 205, 30))

    # if hovering_id:
        # opened_text = title_font.render(
        #    notes[ids.index(hovering_id)], True, BLACK)
        # opened_text = ids.index(hovering_id)
    # make sure that your actually hovering over something
    if hovering_id != None:
        opening = True
        openingid = hovering_id
        pass
    else:
        opening = False

    if opening:
        # create drop down menu to show the notes under the button
        # open frame is x open height is y in a quadratic equation
        open_frame += 1
        if open_frame <= 60:
            open_height += .9
        elif open_frame <= 80:
            open_height += .8
        elif open_frame <= 100:
            open_height += .7
        elif open_frame <= 120:
            open_height += .6
        elif open_frame <= 140:
            open_height += .5
        elif open_frame <= 160:
            open_height += .4
        elif open_frame <= 180:
            open_height += .3
        elif open_frame <= 200:
            open_height += .2
        elif open_frame <= 240:
            open_height += .1

        # for every frame in the opening of the note drop down
        for height in heights:
            if mouse_x >= (WIDTH // 2) - 125 and mouse_x <= (WIDTH // 2) + 80 and mouse_y >= (HEIGHT // 2) + int(height) - 205 and mouse_y <= (HEIGHT // 2) + int(height) - 175:
                pygame.draw.rect(screen, (191, 144, 0), ((
                    WIDTH // 2) - 125, (HEIGHT // 2) + int(height) - 205, 205, 30 + open_height))
                pygame.draw.rect(screen, (255, 240, 200), ((WIDTH // 2) - 125,
                                                           (HEIGHT // 2) + int(height) - 205, 205, 30))
                if notes[ids.index(hovering_id)].__contains__('((('):
                    if len(notes[ids.index(hovering_id)].split(')))')[0][3:]) < 20:
                        title_text = notes[ids.index(hovering_id)].split(')))')[
                            0][3:]
                    else:
                        title_text = notes[ids.index(hovering_id)].split(')))')[
                            0][3:17] + '...'
                else:
                    if len(notes[ids.index(hovering_id)]) > 20:
                        title_text = notes[ids.index(
                            hovering_id)][0:17] + '...'
                    else:
                        title_text = notes[ids.index(hovering_id)]
                # create drop down titles
                screen.blit(title_font.render(title_text, True, BLACK),
                            ((WIDTH // 2) - 120, (HEIGHT // 2) + int(height) - 210))
                # create the notes in the drop downs
                if open_frame >= 240:  # check to make sure the drop down has completed
                    if notes[ids.index(hovering_id)].__contains__('((('):
                        screen.blit(font.render(notes[ids.index(hovering_id)].split(')))')[
                            1], True, BLACK), ((WIDTH // 2) - 120, (HEIGHT // 2) + int(height) - 100))
                    else:
                        screen.blit(font.render(notes[ids.index(hovering_id)], True, BLACK), ((
                            WIDTH // 2) - 120, (HEIGHT // 2) + int(height) - 100))

    else:
        open_height = 0
        open_frame = 0
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


# # # # # # # # # # # # # # # NEXT STEP: create boxes around the titles and make it so that wehn you hover over the boxes it creates a drop down
# # # # # # # # # # # # # # # showing the title of the note and everything in it and when you take your mouse off it it close again
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
