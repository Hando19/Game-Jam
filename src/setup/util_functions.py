import pygame

def get_sprite(img_path, row, column, width, height, scale):
        """
        Extracts a single sprite from a spritesheet.

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
