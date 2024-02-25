import pygame
from setup.game_setup import screen_height, screen_width

def get_sprite(img_path, row, column, width, height, scale):
        """
        Extracts a single sprite from a spritesheet.

        :param image: Contains image path of spritesheet
        :param row: The row in the spritesheet where the sprite is located.
        :param column: The column in the spritesheet where the sprite is located.
        :param width: The width of the sprite.
        :param height: The height of the sprite.
        :return: A Surface object representing the sprite.
        """

        image = pygame.image.load(img_path).convert_alpha()
        sprite_x = column * width
        sprite_y = row * height
        sprite = image.subsurface(pygame.Rect(sprite_x, sprite_y, width, height))

        return pygame.transform.scale(sprite, (scale, scale))

def prepare_background(background, single_sprite):
    """
    Prepares the background surface with a sprite and returns it.

    :param background: The background surface to draw on.
    :param single_sprite: An instance containing sprite image.
    """
    for x in range(0, screen_width, 50):  # Assuming each sprite is 50x50 pixels
        for y in range(0, screen_height, 50):
            background.blit(single_sprite, (x, y))
    return background

def get_scaled_image(img_path, scale):
        full_image = pygame.image.load(img_path).convert_alpha()
        scaled_image = pygame.transform.scale(full_image, (scale, scale))
        
        return scaled_image