import pygame
from setup.game_setup import wall_dimentions
from setup.util_functions import get_sprite, get_scaled_image

class HouseSprites:
    def __init__(self):
        self.img_path = 'src/assets/HouseAssets.png'
        self.grass_img_path = 'src/assets/Grass.png'

    #outter house roofing
    def get_bottom_roof(self):
        return get_sprite(self.img_path, 3, 4, 20, 18, wall_dimentions)

    def get_upper_roof(self):
        return pygame.transform.rotate(self.get_bottom_roof(), 180)

    def get_left_roof(self):
        return pygame.transform.rotate(self.get_bottom_roof(), 270)

    def get_right_roof(self):
        return pygame.transform.rotate(self.get_bottom_roof(), 90)

    #inner house walls
    def get_vertical_inner_wall(self):
        return get_sprite(self.img_path, 2, 2, 8, 8, wall_dimentions)
    
    def get_horizontal_inner_wall(self):
        return pygame.transform.rotate(self.get_vertical_inner_wall(), 90)

    #One off sprites
    def get_floor(self):
        return get_sprite(self.img_path, 2, 2, 10, 16, wall_dimentions)

    def get_door(self):
        return get_sprite(self.img_path, 2, 2, 22, 10, wall_dimentions)

    def get_grass(self):
        return get_scaled_image(self.grass_img_path, wall_dimentions)