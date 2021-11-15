import pygame
from player import Player
from collectable import Collectable

# Constants
WIN_SIZE = (800, 600)
PLAYER_SIZE = 12                            # Default player's size (the game will scale according to the size)
PLAYER_SPEED = 7                            # Default player's speed
BACKGROUND_COLOR = (255, 255, 255)          # White
COLOR1 = (142, 157, 62)                     # Grey
COLOR2 = (100, 45, 200)                    # Grey

# Initialize game's window
pygame.init()
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Snake Race, by Din Ezra")
isGameOn = True

# Initialize player's Snake
player = (
    Player(0, (WIN_SIZE[0]*0.75, WIN_SIZE[1]/2), COLOR1, PLAYER_SIZE, PLAYER_SPEED),
    Player(1, (WIN_SIZE[0]*0.25, WIN_SIZE[1]/2), COLOR2, PLAYER_SIZE, PLAYER_SPEED))

# Initialize collectables
coin = Collectable(WIN_SIZE, (player[0].body.head, player[1].body.head), PLAYER_SIZE // 2)


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
            for p in player:
                p.changeDirection(event.key)

    for p in player:
        # Collision Detection:
        if collisionDetection(p.body.head.data, p.size, coin.position, coin.size):
            p.body.addToEnd(coin.position)
            p.score += 1
            coin = Collectable(WIN_SIZE, (player[0].body.head, player[1].body.head), PLAYER_SIZE // 2)

        # Update the Player's object:
        p.update()

    # Update the collectable object:
    coin.update()


def drawGame():
    gameDisplay.fill(BACKGROUND_COLOR)
    for p in player:
        p.draw(gameDisplay)
    coin.draw(gameDisplay)
    pygame.display.update()


""" Game's Loop """
while isGameOn:

    updateGame()
    drawGame()
    clock.tick(30)

pygame.quit()
quit()
