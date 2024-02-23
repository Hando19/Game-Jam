import pygame
from classes.coin import Coin
from setup.player import player_image

player_size = 50;

coins = [
    Coin((415, 200)),
    Coin((88, 510))
]

def find_nearest_safe_position(coin_pos, walls):
    search_radius = 20  # Distance in pixels to search around the coin
    for dx in range(-search_radius, search_radius + 1, 10): 
        for dy in range(-search_radius, search_radius + 1, 10):
            potential_pos = (coin_pos[0] + dx, coin_pos[1] + dy)
            potential_rect = pygame.Rect(potential_pos[0], potential_pos[1], player_size, player_size)
            if not any(potential_rect.colliderect(wall) for wall in walls):
                return potential_pos  # Return the first non-colliding position
    return coin_pos  # Fallback to the coin's position if no safe spot is found