import pygame
from setup.game_setup import projectile_dimentions, nest_dimensions
from setup.util_functions import get_sprite, get_scaled_image

class AnimalSprites:
    def __init__(self):
        self.animal_img_path = 'src/assets/AnimalAssets.png'
        self.insect_nest_img_path = 'src/assets/InsectNest.png'
        self.insect_img_path = 'src/assets/Insect.png'
        self.bear_img_path = 'src/assets/Bear.png'

    #mouse sprites
    def get_mouse_right_face(self):
        return get_sprite(self.animal_img_path, 12, 12, 16, 12.5, projectile_dimentions)
    
    def get_mouse_left_face(self):
        return pygame.transform.flip(self.get_mouse_right_face(), True, False)
    
    def get_mouse_upward_face(self):
        return pygame.transform.rotate(self.get_mouse_right_face(), 90)
    
    def get_mouse_downward_face(self):
        return pygame.transform.rotate(self.get_mouse_left_face(), 90)

    #insect nest
    def get_insect_nest(self):
        return get_scaled_image(self.insect_nest_img_path, nest_dimensions)
    
    #insect sprites
    def get_insect_right_face(self):
        return get_scaled_image(self.insect_img_path, 30)
    
    def get_insect_left_face(self):
        return pygame.transform.flip(self.get_insect_right_face(), True, False)
    
    def get_insect_upward_face(self):
        return pygame.transform.rotate(self.get_insect_right_face(), 90)
    
    def get_insect_downward_face(self):
        return pygame.transform.rotate(self.get_insect_left_face(), 90)
    
    #bear sprites
    def get_bear_right_face(self):
        return get_scaled_image(self.bear_img_path, projectile_dimentions)
    
    def get_bear_left_face(self):
        return pygame.transform.flip(self.get_bear_right_face(), True, False)
    
    def get_bear_upward_face(self):
        return pygame.transform.rotate(self.get_bear_right_face(), 90)
    
    def get_bear_downward_face(self):
        return pygame.transform.rotate(self.get_bear_left_face(), 90)