import pygame
import sys

from setup.game_setup import screen, black, gray
from setup.player import player_speed, player_image
from Laundry.wall_manager import walls
from Laundry.projectile_manager import projectiles
from Laundry.coin_manager import coins, find_nearest_safe_position

def laundry_level():
    # Adjusted player spawn position
    player_start_pos = (75, 75)  # Define the player's starting position
    player_rect = player_image.get_rect(topleft=player_start_pos)

    next_level_block = pygame.Rect(660, 60, 30, 40) 
    next_level_block_shown = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)  # Clear screen

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

        # Draw walls
        for wall in walls:
            pygame.draw.rect(screen, gray, wall)  # Draw each wall

        # Collision detection with walls
        collision = False
        for wall in walls:
            if player_rect_test.colliderect(wall):
                collision = True
                break
        
        for coin in coins:
            if player_rect.colliderect(coin.rect) and not coin.collected:
                safe_pos = find_nearest_safe_position(coin.position, walls)
                player_start_pos = safe_pos  # Update player's reset position to a safe location
                coin.collected = True

        # Update and draw projectiles
        for projectile in projectiles:
            projectile.update()
            projectile.draw(screen)
            
            # Check collision with the player
            if player_rect.colliderect(projectile.rect):
                player_rect.topleft = player_start_pos  # Reset player position if hit
            if not collision:
                player_rect = player_rect_test

        # Draw coins
        for coin in coins:
            coin.draw(screen)

        all_coins_collected = all(coin.collected for coin in coins)
        if all_coins_collected and not next_level_block_shown:
            next_level_block_shown = True

        if next_level_block_shown:
            pygame.draw.rect(screen, (0, 255, 0), next_level_block)  

        if next_level_block_shown and player_rect.colliderect(next_level_block):
            # Code to transition to the next level
            print("Transition to the next level!")  

        # Draw the player
        screen.blit(player_image, player_rect)

        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(60)  # Cap the frame rate