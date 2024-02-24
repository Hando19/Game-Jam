import pygame
from setup.game_setup import projectile_dimentions
from setup.util_functions import get_sprite

class AnimalSprites:
    def __init__(self):
        self.img_path = 'src/assets/AnimalAssets.png'

    #mouse animation
    def get_mouse_right_face(self):
        return get_sprite(self.img_path, 12, 12, 16, 12.5, projectile_dimentions)
    
    def get_mouse_left_face(self):
        return pygame.transform.flip(self.get_mouse_right_face(), True, False)
    
    def get_mouse_upward_face(self):
        return pygame.transform.rotate(self.get_mouse_right_face(), 90)
    
    def get_mouse_downward_face(self):
        return pygame.transform.rotate(self.get_mouse_left_face(), 90)
