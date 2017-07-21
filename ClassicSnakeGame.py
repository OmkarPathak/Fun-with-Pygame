# Author: OMKAR PATHAK

import pygame, sys
from pygame.locals import *
import time
import random

# required
pygame.init()

# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

# required globals
window_width = 800
window_height = 600
FPS = 20                        # Frames per seconds

# setting the display size
DISPLAYSURF = pygame.display.set_mode((window_width, window_height))
# setting th caption
pygame.display.set_caption('Arbok')
# loading the snake image
img = pygame.image.load('snake.png')
# snake head direction
direction = 'right'

def game_startup_screen():
    intro = True
    while intro:
        # get which key is pressed
        for event in pygame.event.get():
            # if the X(close button) in the menu pane is pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # if Q is pressed
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                # if C is pressed
                if event.key == pygame.K_c:
                    intro = False

        # fill the whole displat with white color
        DISPLAYSURF.fill(WHITE)
        display_message_on_screen('Welcome to Arbok!!', BLUE, -100)
        display_message_on_screen('Press C to Play and Q to Quit', BLUE, -70)
        pygame.display.update()

def display_message_on_screen(message, color, y_displace = 0):
    # set the font
    font = pygame.font.SysFont('freemono', 25)
    text = font.render(message, True, color)
    textRect = text.get_rect()
    # write the text in center of the window
    textRect.center = (window_width // 2), (window_height // 2) + y_displace
    DISPLAYSURF.blit(text, textRect)

def snake(coord_list, global_coord_offset):
    # check the direction of snake's head to rotate accordingly
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)

    # display head
    DISPLAYSURF.blit(head, (coord_list[-1][0], coord_list[-1][1]))
    # display body
    for coord in coord_list[:-1]:
        pygame.draw.rect(DISPLAYSURF, BLACK, [coord[0], coord[1], global_coord_offset, global_coord_offset])

def start_game():
    # required variables
    global direction
    direction = 'right'                 # snake's head will point at right direction on each startup

    # get the center of the screen
    x_coord = window_width // 2
    y_coord = window_height // 2

    # declaring offset to move the snake
    x_coord_offset = 0
    y_coord_offset = 0

    # declaring the number of pixels snake will move on each move
    global_coord_offset = 10

    # for setting frames per sec
    clock = pygame.time.Clock()

    # for storing the snake's body
    coord_list = []
    snakeLength = 1

    # snake's food coordinates
    food_x_coord = round(random.randrange(0, window_width - global_coord_offset) // 10.0) * 10.0
    food_y_coord = round(random.randrange(0, window_height - global_coord_offset) // 10.0) * 10.0

    exit = False
    game_over = False

    while not exit:                 # main game loop
        DISPLAYSURF.fill(WHITE)

        # this loop will execute when game is over
        while game_over == True:
            display_message_on_screen('GAME OVER', RED)
            display_message_on_screen('Press C to Continue and Q to Quit', BLACK, 50)
            pygame.display.update()

            # get which key is pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        start_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            # if key is pressed
            if event.type == pygame.KEYDOWN:
                # if left arrow key is pressed move to left
                if event.key == pygame.K_LEFT:
                    x_coord_offset = -global_coord_offset
                    y_coord_offset = 0
                    direction = 'left'
                # if right arrow key is pressed move to right
                elif event.key == pygame.K_RIGHT:
                    x_coord_offset = global_coord_offset
                    y_coord_offset = 0
                    direction = 'right'
                # if right arrow key is pressed move to right
                elif event.key == pygame.K_UP:
                    y_coord_offset = -global_coord_offset
                    x_coord_offset = 0
                    direction = 'up'
                # if right arrow key is pressed move to right
                elif event.key == pygame.K_DOWN:
                    y_coord_offset = global_coord_offset
                    x_coord_offset = 0
                    direction = 'down'

            # defining boundaries
            if abs(x_coord) >= window_width or x_coord <= 0 or abs(y_coord) >= window_height or y_coord <= 0:
                game_over = True

        # move snake with specified offset
        x_coord += x_coord_offset
        y_coord += y_coord_offset

        # pygame.draw.rect(where_do_you_wanna_draw, color, [x_coord, y_coord, width, height])
        pygame.draw.rect(DISPLAYSURF, RED, [food_x_coord, food_y_coord, global_coord_offset, global_coord_offset])

        coord_head = []
        coord_head.append(x_coord)
        coord_head.append(y_coord)
        coord_list.append(coord_head)

        if len(coord_list) > snakeLength:
            del coord_list[0]

        # check if snake touches it's own body
        for current_coord in coord_list[:-1]:
            if current_coord == coord_head:
                game_over = True

        snake(coord_list, global_coord_offset)

        pygame.display.update()

        # if snake eats the food
        if x_coord == food_x_coord and y_coord == food_y_coord:
            food_x_coord = round(random.randrange(0, window_width - global_coord_offset) // 10.0) * 10.0
            food_y_coord = round(random.randrange(0, window_height - global_coord_offset) // 10.0) * 10.0
            snakeLength += 1

        # regulating the game speed
        clock.tick(FPS)

    time.sleep(2)
    pygame.quit()
    quit()

game_startup_screen()
start_game()
