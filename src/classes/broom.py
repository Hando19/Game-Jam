import pygame
from setup.game_setup import broom_dimensions

class Broom:
    def __init__(self, position):
        self.img_path = 'src/assets/Broom.png'
        self.position = position
        self.collected = False
        self.rect = pygame.Rect(position[0], position[1], broom_dimensions, broom_dimensions)
        self.broom_image = self.get_scaled_broom()

    def get_scaled_broom(self):
        broom_image_full = pygame.image.load(self.img_path).convert_alpha()
        scaled_broom = pygame.transform.scale(broom_image_full, (self.rect.width, self.rect.height))
        
        return scaled_broom

    def draw(self, surface):
        if not self.collected:
            surface.blit(self.broom_image, self.rect.topleft)

