import pygame
from setup.game_setup import red

class MovableObject:
    def __init__(self, x, y, width=50, height=50):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = red

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, dx, dy):
        """Move the object by dx and dy."""
        self.rect.x += dx
        self.rect.y += dy

    def is_collided_with(self, other_rect):
        """Check if this object is colliding with another rectangle."""
        return self.rect.colliderect(other_rect)
