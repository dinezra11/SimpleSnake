from linkedList import LinkedList, Node
import pygame


class Player:
    def __init__(self, position: tuple, color=(0, 0, 0), size=5, speed=5):
        self.body = LinkedList()
        self.body.addToFront(position)
        self.color = color
        self.size = size
        self.speed = speed
        self.direction = (speed, 0) # starting movement is set to the RIGHT

    def update(self):
        node = self.body.tail
        while node != self.body.head:
            node.data = (node.prev.data[0], node.prev.data[1])

        newPosition = (self.body.head.data[0] + self.direction[0], self.body.head.data[1] + self.direction[1])
        self.body.head.data = newPosition

    def draw(self, display: pygame.Surface):
        pygame.draw.circle(display, self.color, self.body.head.data, self.size)
