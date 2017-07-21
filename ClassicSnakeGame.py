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

game_startup_screen()
