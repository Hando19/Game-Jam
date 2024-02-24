import pygame
import sys
from setup.game_setup import screen, screen_height, screen_width
from HouseCleaning.wall_manager import walls, draw_walls
from HouseCleaning.projectile_manager import projectiles
from HouseCleaning.broom_manager import brooms, find_nearest_safe_position
from classes.houseSprites import HouseSprites
from setup.player import Player

def house_level():
    house_sprites = HouseSprites()
    player = Player()

    # Adjusted player spawn position
    player_start_pos = (75, 75)
    player_rect = player.update_spawn_position((75, 75))

    next_level_block = pygame.Rect(650, 60, 20, 40) 
    next_level_block_shown = False

    # Create a background surface
    background = pygame.Surface((screen_width, screen_height))

    # Filling background with floor sprite
    for x in range(0, screen_width, 50):
        for y in range(0, screen_height, 50):
            background.blit(house_sprites.get_floor(), (x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        proposed_move = player.propose_move()

        # Blit the background surface to the screen at the start of each frame
        screen.blit(background, (0, 0))

        draw_walls(screen)

        # Collision detection with walls
        collision = any(proposed_move.colliderect(wall) for wall in walls)

        # If there's no collision detected, update the player's actual position
        if not collision:
            player.update_hitbox_rect(proposed_move)

        for broom in brooms:
            if player.get_hitbox_rect().colliderect(broom.rect) and not broom.collected:
                safe_pos = find_nearest_safe_position(broom.position, walls)
                player_start_pos = safe_pos  # Update player's reset position to a safe location
                broom.collected = True

        # Update and draw projectiles
        for projectile in projectiles:
            projectile.update()
            projectile.draw(screen)
            
            if player.get_hitbox_rect().colliderect(projectile.rect):
                player.update_spawn_position(player_start_pos) 

        # Draw brooms
        for broom in brooms:
            broom.draw(screen)
        
        all_brooms_collected = all(broom.collected for broom in brooms)
        if all_brooms_collected and not next_level_block_shown:
            next_level_block_shown = True

        if next_level_block_shown:
            screen.blit(house_sprites.get_door(), next_level_block)

        if next_level_block_shown and player.get_hitbox_rect().colliderect(next_level_block):
            running = False 

        player.draw(screen)   # Draw the player sprite to the screen

        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(60)  # Cap the frame rate
