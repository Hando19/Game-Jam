import pygame
from classes.broom import Broom
from setup.player import player_image

player_size = 50

brooms = [
    #closest broom, upper middle
    Broom((408, 190)),

    #lower left corner broom
    Broom((73, 500)),

    #middle bottom broom
    Broom((480, 410))
]

def find_nearest_safe_position(broom_pos, walls):
    search_radius = 20  # Distance in pixels to search around the coin
    for dx in range(-search_radius, search_radius + 1, 10): 
        for dy in range(-search_radius, search_radius + 1, 10):
            potential_pos = (broom_pos[0] + dx, broom_pos[1] + dy)
            potential_rect = pygame.Rect(potential_pos[0], potential_pos[1], player_size, player_size)
            if not any(potential_rect.colliderect(wall) for wall in walls):
                return potential_pos  # Return the first non-colliding position
    return broom_pos  # Fallback to the coin's position if no safe spot is found