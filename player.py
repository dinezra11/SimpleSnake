from linkedList import LinkedList
import pygame


class Player:
    def __init__(self, position: tuple, color=(0, 0, 0), size=10, speed=7):
        self.body = LinkedList()
        self.body.addToFront(position)
        self.color = color
        self.size = size
        self.speed = speed
        self.direction = (speed, 0) # starting movement is set to the RIGHT
        self.score = 0

    def changeDirection(self, key):
        """ Change the direction of the snake. Key = the pygame's constant that indicates the key pressed. """
        if key == pygame.K_UP and self.direction[1] <= 0:
            self.direction = (0, -self.speed)
        elif key == pygame.K_DOWN and self.direction[1] >= 0:
            self.direction = (0, self.speed)
        elif key == pygame.K_LEFT and self.direction[0] <= 0:
            self.direction = (-self.speed, 0)
        elif key == pygame.K_RIGHT and self.direction[0] >= 0:
            self.direction = (self.speed, 0)

    def update(self):
        node = self.body.tail
        while node != self.body.head:
            node.data = (node.prev.data[0], node.prev.data[1])
            node = node.prev

        newPosition = (self.body.head.data[0] + self.direction[0], self.body.head.data[1] + self.direction[1])
        self.body.head.data = newPosition

    def draw(self, display: pygame.Surface):
        node = self.body.head
        while node is not None:
            pygame.draw.rect(display, self.color, (node.data[0], node.data[1], self.size, self.size))
            node = node.next
