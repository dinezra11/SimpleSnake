import pygame
from player import Player
from collectable import Collectable

# Constants
WIN_SIZE = (800, 600)
PLAYER_SIZE = 12                            # Default player's size (the game will scale according to the size)
PLAYER_SPEED = 7                            # Default player's speed
BACKGROUND_COLOR = (255, 255, 255)          # White
COLOR = (142, 157, 62)                      # Grey

# Initialize game's window
pygame.init()
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Snake Race, by Din Ezra")
isGameOn = True

# Initialize player's Snake
player = Player((WIN_SIZE[0]/2, WIN_SIZE[1]/2), COLOR, PLAYER_SIZE, PLAYER_SPEED)

# Initialize collectables
coin = Collectable(WIN_SIZE, (player.body.head, player.body.head), PLAYER_SIZE // 2)


def collisionDetection(pos1, size1, pos2, size2):
    """ Detect a collision between 2 objects.
    parameters: position (tuple) and size (int) of 2 objects.
    """
    for i in range(2):
        if pos1[i] > pos2[i] + size2 or pos1[i] + size1 < pos2[i]:
            return False

    return True


def updateGame():
    global isGameOn, coin

    # Get User's Input:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameOn = False
        if event.type == pygame.KEYDOWN:
            player.changeDirection(event.key)

    # Collision Detection:
    if collisionDetection(player.body.head.data, player.size, coin.position, coin.size):
        player.body.addToEnd(coin.position)
        player.score += 1
        coin = Collectable(WIN_SIZE, (player.body.head, player.body.head), PLAYER_SIZE // 2)

    # Update objects:
    player.update()
    coin.update()


def drawGame():
    gameDisplay.fill(BACKGROUND_COLOR)
    player.draw(gameDisplay)
    coin.draw(gameDisplay)
    pygame.display.update()


""" Game's Loop """
while isGameOn:

    updateGame()
    drawGame()
    clock.tick(30)

pygame.quit()
quit()
