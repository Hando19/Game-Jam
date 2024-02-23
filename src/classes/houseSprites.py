import pygame
from setup.game_setup import wall_dimentions

class HouseSprites:
    def __init__(self):
        self.img_path = 'src/assets/HouseAssets.png'

    def get_sprite(self, row, column, width, height):
        """
        Extracts a single sprite from a spritesheet.

        :param row: The row in the spritesheet where the sprite is located.
        :param column: The column in the spritesheet where the sprite is located.
        :param width: The width of the sprite.
        :param height: The height of the sprite.
        :return: A Surface object representing the sprite.
        """
        spritesheet = pygame.image.load(self.img_path).convert_alpha()
        sprite_x = column * width
        sprite_y = row * height
        sprite = spritesheet.subsurface(pygame.Rect(sprite_x, sprite_y, width, height))

        return pygame.transform.scale(sprite, (wall_dimentions, wall_dimentions))

    #outter house roofing
    def get_bottom_roof(self):
        return self.get_sprite(3, 4, 20, 18)

    def get_upper_roof(self):
        return pygame.transform.rotate(self.get_bottom_roof(), 180)

    def get_left_roof(self):
        return pygame.transform.rotate(self.get_bottom_roof(), 270)

    def get_right_roof(self):
        return pygame.transform.rotate(self.get_bottom_roof(), 90)

    #inner house corners
    def get_upper_right_corner(self):
        return self.get_sprite(1, 1, 18, 18)

    def get_upper_left_corner(self):
        return pygame.transform.rotate(self.get_upper_right_corner(), 90)

    def get_bottom_left_corner(self):
        return pygame.transform.rotate(self.get_upper_right_corner(), 180)

    def get_bottom_right_corner(self):
        return pygame.transform.rotate(self.get_upper_right_corner(), 270)

    #inner house walls
    def get_right_inner_wall(self):
        return self.get_sprite(2, 2, 13, 16)
    
    def get_upper_inner_wall(self):
        return pygame.transform.rotate(self.get_right_inner_wall(), 90)

    def get_left_inner_wall(self):
        return pygame.transform.rotate(self.get_right_inner_wall(), 180)

    def get_bottom_inner_wall(self):
        return pygame.transform.rotate(self.get_right_inner_wall(), 270)
    
    #inner house walls
    def get_test(self):
        return self.get_sprite(2, 2, 8, 8)
    
    #flooring
    def get_floor(self):
        return self.get_sprite(2, 2, 10, 16)