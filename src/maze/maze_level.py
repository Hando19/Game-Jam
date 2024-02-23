import pygame
import sys

from setup.game_setup import screen, black, gray
from setup.player import player_speed, player_image
from maze.wall_manager import walls

def maze_level():
    # Adjusted player spawn position
    player_rect = player_image.get_rect(topleft=(75, 75)) 

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

        if not collision:
            player_rect = player_rect_test

        # Draw the player
        screen.blit(player_image, player_rect)

        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(60)  # Cap the frame rate
