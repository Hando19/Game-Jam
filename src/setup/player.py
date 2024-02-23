import pygame
from setup.game_setup import white

# Load Player Sprite
player_image = pygame.Surface((50, 50))  # Placeholder for player sprite
player_image.fill(white)
player_rect = player_image.get_rect(topleft=(75, 75))  # Adjusted player spawn position

# Player properties
player_speed = 5