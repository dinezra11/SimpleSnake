from linkedlist import LinkedList, Node
import pygame


class Player:
    def __init__(self, position: tuple, color=(0, 0, 0), size=5, speed=5):
        self.body = LinkedList()
        self.body.add(position)
        self.color = color
        self.size = size
        self.speed = speed
        self.direction = (speed, 0) # starting movement is set to the RIGHT

    """def update(self):
        node = self.body.head
        while node.next is not Node:"""


    def draw(self, display: pygame.Surface):
        pygame.draw.circle(display, self.color, self.body.head.data, self.size)