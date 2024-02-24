import pygame
import sys

from setup.game_setup import screen, screen_height, screen_width
from setup.player import player_speed, player_image
from HouseCleaning.wall_manager import walls, draw_walls
from HouseCleaning.projectile_manager import projectiles
from HouseCleaning.broom_manager import brooms, find_nearest_safe_position
from classes.houseSprites import HouseSprites

def house_level():
    house_sprites = HouseSprites()

    # Adjusted player spawn position
    player_start_pos = (75, 75)  # Define the player's starting position
    player_rect = player_image.get_rect(topleft=player_start_pos)

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

        # Key press handling
        keys = pygame.key.get_pressed()
        player_rect_test = player_rect.copy()
        if keys[pygame.K_LEFT]:
            player_rect_test.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect_test.x += player_speed
        if keys[pygame.K_UP]:
            player_rect_test.y -= player_speed
        if keys[pygame.K_DOWN]:
            player_rect_test.y += player_speed

        # Blit the background surface to the screen at the start of each frame
        screen.blit(background, (0, 0))

        draw_walls(screen)

        # Collision detection with walls
        collision = False
        for wall in walls:
            if player_rect_test.colliderect(wall):
                collision = True
                break
        
        for broom in brooms:
            if player_rect.colliderect(broom.rect) and not broom.collected:
                safe_pos = find_nearest_safe_position(broom.position, walls)
                player_start_pos = safe_pos  # Update player's reset position to a safe location
                broom.collected = True

        # Update and draw projectiles
        for projectile in projectiles:
            projectile.update()
            projectile.draw(screen)
            
            # Check collision with the player
            if player_rect.colliderect(projectile.rect):
                player_rect.topleft = player_start_pos  # Reset player position if hit
            if not collision:
                player_rect = player_rect_test

        # Draw brooms
        for broom in brooms:
            broom.draw(screen)
        
        all_brooms_collected = all(broom.collected for broom in brooms)
        if all_brooms_collected and not next_level_block_shown:
            next_level_block_shown = True

        if next_level_block_shown:
            screen.blit(house_sprites.get_door(), next_level_block)

        if next_level_block_shown and player_rect.colliderect(next_level_block):
            running = False 

        # Draw the player
        screen.blit(player_image, player_rect)

        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(60)  # Cap the frame rate
