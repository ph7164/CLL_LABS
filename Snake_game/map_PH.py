# Snake Game

import sys
import pygame
from pygame.locals import *


# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = (400, 300)
screen = pygame.display.set_mode(size, DOUBLEBUF)

pos_x = 200
pos_y = 200

pygame.display.set_caption("Game Title")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    # Main Event Loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
            sys.exit()


    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 1

    if key_event[pygame.K_RIGHT]:
        pos_x += 1

    if key_event[pygame.K_DOWN]:
        pos_y += 1

    if key_event[pygame.K_UP]:
        pos_y -= 1
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    font = pygame.font.Font(None, 36)
    text = font.render("Hello there", 1, (0, 0, 0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    screen.blit(background, (0, 0))

    pygame.draw.circle(screen, RED, (pos_x, pos_y), 20)

    pygame.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 5)
    pygame.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 0)
    pygame.draw.lines(screen, RED, False, [[50, 150], [50, 250], [200, 250], [200, 150]], 5)
    pygame.draw.rect(screen, BLACK, [75, 175, 75, 50], 5)
    pygame.draw.rect(screen, BLUE, [75, 175, 75, 50], 0)
    pygame.draw.line(screen, BLACK, [112, 175], [112, 225], 5)
    pygame.draw.line(screen, BLACK, [75, 200], [150, 200], 5)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
