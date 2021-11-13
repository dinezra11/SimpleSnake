import pygame
from player import Player

# Constants
WIN_SIZE = (800, 600)
BACKGROUND_COLOR = (255, 255, 255)          # White
COLOR = (142, 157, 62)                      # Grey

# Initialize game's window
pygame.init()
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Simple Snake, by Din Ezra")
isGameOn = True

# Initialize player's Snake
player = Player((WIN_SIZE[0]/2, WIN_SIZE[1]/2), COLOR)

while isGameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameOn = False

    gameDisplay.fill(BACKGROUND_COLOR)
    player.draw(gameDisplay)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
