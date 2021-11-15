import pygame
import random
from linkedList import LinkedList


class Collectable:
    def __init__(self, screenSize: tuple, snakesPositions: tuple, size=5):
        """ Constructor of the Collectable object.

        :param screenSize: A tuple which indicates the size of the screen. Used to generate a random position within
            the screen's borders.
        :param snakesPositions: A tuple. Each member is a linked list of a player's snake position.
        :param size: The size of the collectable.
        """
        def generatePosition():
            """ Generate a new random position for the collectable.
            Return TRUE if the position is legal. Return FALSE if the position is illegal. """

            self.position = (random.randint(0, screenSize[0] - self.size), random.randint(0, screenSize[1] - self.size))
            for i in range(len(snakesPositions)):
                # Run for each player:
                linkedList = snakesPositions[i]

                while linkedList is not None:
                    if linkedList.data == self.position:
                        return False

                    linkedList = linkedList.next

            return True

        self.size = size
        self.type = "collectable"

        # Generate random position:
        while not generatePosition():
            pass # Do nothing. The loop will end when the function will return 'True'

        # Generate random color
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self):
        if self.type == "boost":
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, display: pygame.Surface):
        pygame.draw.circle(display, self.color, self.position, self.size)
