import pygame
from player import Player
from collectable import Collectable

# Constants
WIN_SIZE = (800, 600)
PLAYER_SIZE = 12                                    # Default player's size (the game will scale according to the size)
PLAYER_SPEED = 7                                    # Default player's speed
BACKGROUND_COLOR = (200, 200, 200)                  # Default background color
COLOR1 = (142, 157, 62)                             # First player color
COLOR2 = (100, 45, 200)                             # Second player color
COLLECTABLE_RESPAWNRATE = 2500                      # Default respawn rate of the collectables (in milliseconds)
COLLECTABLE_RESPAWNEVNT = pygame.USEREVENT+1        # The timed event ID
MAX_COLLECTABLES = 5                                # Maximum collectables to appear in the game

# Initialize game's window
pygame.init()
gameDisplay = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Snake Race, by Din Ezra")
isGameOn = True

# Time and Clock components
clock = pygame.time.Clock()
pygame.time.set_timer(COLLECTABLE_RESPAWNEVNT, COLLECTABLE_RESPAWNRATE)

# Initialize player's Snake
player = (
    Player(0, (WIN_SIZE[0]*0.25, WIN_SIZE[1]/2), COLOR1, PLAYER_SIZE, PLAYER_SPEED),
    Player(1, (WIN_SIZE[0]*0.75, WIN_SIZE[1]/2), COLOR2, PLAYER_SIZE, PLAYER_SPEED))

# Initialize collectables
coin = [
    Collectable(WIN_SIZE, (player[0].body.head, player[1].body.head), PLAYER_SIZE // 2)]


def collisionDetection(pos1, size1, pos2, size2):
    """ Detect a collision between 2 objects.
    parameters: position (tuple) and size (int) of 2 objects.
    """
    for i in range(len(pos1)):
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
        if event.type == COLLECTABLE_RESPAWNEVNT and len(coin) <= MAX_COLLECTABLES:
            coin.append(Collectable(WIN_SIZE, (player[0].body.head, player[1].body.head), PLAYER_SIZE // 2))

    for p in player:
        # Update the Player's object:
        p.update()

        for i in range(len(coin)):
            # Update the collectable object:
            coin[i].update()

            # Collision Detection:
            if collisionDetection(p.body.head.data, p.size, coin[i].position, coin[i].size):
                p.body.addToEnd(coin[i].position)
                p.score += 1
                coin.pop(i)
                break


def drawGame():
    gameDisplay.fill(BACKGROUND_COLOR)
    for p in player:
        p.draw(gameDisplay)
    for c in coin:
        c.draw(gameDisplay)
    pygame.display.update()


""" Game's Loop """
while isGameOn:
    updateGame()
    drawGame()
    clock.tick(30)

# Game end! Show results:

pygame.quit()
quit()
