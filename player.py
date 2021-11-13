import pygame


class Player:

    def __init__(self, position: tuple):
        self.posX, self.posY = position
        self.moveX = self.moveY = 0
        self.snakeImg = pygame.image.load("")

    def update(self):
        self.posX += self.moveX
        self.posY += self.moveY

    def draw(self, display: pygame.Surface):
        display.blit(display, snakeImg, (self.posX, self.posY))
