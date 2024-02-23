import pygame

class Coin:
    def __init__(self, position):
        self.position = position
        self.collected = False
        self.rect = pygame.Rect(position[0], position[1], 20, 20)

    def draw(self, surface):
        if not self.collected:
            pygame.draw.circle(surface, (255, 215, 0), self.position, 10) 
