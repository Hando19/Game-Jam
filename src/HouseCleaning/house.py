import pygame
import sys
from setup.game_setup import screen, screen_height, screen_width
from setup.util_functions import prepare_background
from HouseCleaning.wall_manager import walls, draw_walls
from HouseCleaning.projectile_manager import projectiles
from HouseCleaning.broom_manager import brooms, find_nearest_safe_position
from classes.animalSprites import AnimalSprites
from classes.houseSprites import HouseSprites
from setup.player import Player

def house_level():
    house_sprites = HouseSprites()
    animal_sprites = AnimalSprites()
    player = Player()

    # Adjusted player spawn position
    player_start_pos = (75, 75)

    next_level_block = pygame.Rect(650, 60, 20, 40) 
    next_level_block_shown = False

    # Preparing background using single sprite
    background = pygame.Surface((screen_width, screen_height))
    background = prepare_background(background, house_sprites.get_floor())

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

        # Handling collisions with brooms
        for broom in brooms:
            if player.get_hitbox_rect().colliderect(broom.rect) and not broom.collected:
                safe_pos = find_nearest_safe_position(broom.position, walls)
                player_start_pos = safe_pos  # Update player's reset position to a safe location
                broom.collected = True

        # Update and draw projectiles
        for projectile in projectiles:
            projectile.update()
            projectile.draw_mice(screen)
            
            if player.get_hitbox_rect().colliderect(projectile.rect):
                player.update_spawn_position(player_start_pos) 

        # Draw brooms
        for broom in brooms:
            broom.draw(screen)
        
        # Showing exit door on all broom collection condition
        all_brooms_collected = all(broom.collected for broom in brooms)
        if all_brooms_collected and not next_level_block_shown:
            next_level_block_shown = True

        if next_level_block_shown:
            screen.blit(house_sprites.get_door(), next_level_block)

        if next_level_block_shown and player.get_hitbox_rect().colliderect(next_level_block):
            running = False 

        # Draw the player sprite to the screen
        player.draw(screen)  

        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(60)  # Cap the frame rate
