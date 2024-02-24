import pygame
from setup.game_setup import projectile_dimentions

class AnimalSprites:
    def __init__(self):
        self.img_path = 'src/assets/AnimalAssets.png'

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

        return pygame.transform.scale(sprite, (projectile_dimentions, projectile_dimentions))
    
    #mouse animation
    def get_mouse_right_face(self):
        return self.get_sprite(12, 12, 16, 12.5)
    
    def get_mouse_left_face(self):
        return pygame.transform.flip(self.get_mouse_right_face(), True, False)
    
    def get_mouse_upward_face(self):
        return pygame.transform.rotate(self.get_mouse_right_face(), 90)
    
    def get_mouse_downward_face(self):
        return pygame.transform.rotate(self.get_mouse_left_face(), 90)