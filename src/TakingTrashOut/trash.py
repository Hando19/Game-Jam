import pygame
import sys
import random

from setup.game_setup import black, white, gray, red, dark_gray, screen_height, screen_width, screen, wall_dimentions
from setup.player import Player
from classes.movableObject import MovableObject

# Initialize Pygame font
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Initialize game entities and state
def init_game(player):
    global objects, bullets, collision_count
    objects = []
    num_objects = random.randint(3, 6)
    for _ in range(num_objects):
        x = random.randint(100, screen_width - 100)
        y = random.randint(100, screen_height - 100)
        new_object = MovableObject(x, y)
        while new_object.is_collided_with(player.get_hitbox_rect()):
            new_object.rect.x = random.randint(100, screen_width - 100)
            new_object.rect.y = random.randint(100, screen_height - 100)
        objects.append(new_object)
    bullets = []
    collision_count = 0

# Function to add bullets
def add_bullet():
    y = random.randint(0, screen_height)
    bullet_rect = pygame.Rect(screen_width, y, 10, 10)
    bullets.append(bullet_rect)

def trash_level():
    global collision_count
    collision_count = 0
    player = Player()
    init_game(player)

    # Bullet properties
    bullet_speed = 12

    # Pit properties
    pit_rect = pygame.Rect(200, screen_height - wall_dimentions, 200, wall_dimentions) 

    # Pit hitbox properties (slightly above the pit, same length)
    pit_hitbox_rect = pygame.Rect(pit_rect.x, pit_rect.y, pit_rect.width, 10) 

    # Game loop flag
    running = True
    bullet_timer = 0
    bullet_interval = 60  # Frames until a new bullet is added

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed() 
        proposed_move = player.propose_move()

        # Ensure player remains on screen and adjust for collisions
        proposed_move.x = max(0, min(screen_width - proposed_move.width, proposed_move.x))
        proposed_move.y = max(0, min(screen_height - proposed_move.height, proposed_move.y))

        # Initialize collision flag
        collision = False

        if not collision:
            # If no wall collision, update the player position
            player.update_hitbox_rect(proposed_move)

        for obj in list(objects):  # Using list() to safely modify during iteration
            if proposed_move.colliderect(obj.rect):
                dx = 0
                dy = 0
                if keys[pygame.K_LEFT]: dx = -player.player_speed
                if keys[pygame.K_RIGHT]: dx = player.player_speed
                if keys[pygame.K_UP]: dy = -player.player_speed
                if keys[pygame.K_DOWN]: dy = player.player_speed

                # Calculate the object's new position
                new_x = max(0, min(screen_width - obj.rect.width, obj.rect.x + dx))
                new_y = max(0, min(screen_height - obj.rect.height, obj.rect.y + dy))
                
                # Update the object's position to the new location within bounds
                obj.rect.x = new_x
                obj.rect.y = new_y
                    
            # Check for collision with the pit hitbox and remove the object if collided
            if obj.rect.colliderect(pit_hitbox_rect):
                objects.remove(obj)
                collision_count += 1
        
        # Bullets logic 
        for bullet in bullets[:]:
            bullet.x -= bullet_speed
            if bullet.x < 0:
                bullets.remove(bullet)
            # Check collision with player
            if bullet.colliderect(player.get_hitbox_rect()):
                init_game(player)  # Reset game if player is hit

        bullet_timer += 1
        if bullet_timer >= bullet_interval:
            add_bullet()
            bullet_timer = 0

        # Drawing game elements
        screen.fill(black)

        # Draw the floor, pit, player, and objects
        pygame.draw.rect(screen, dark_gray, (200, screen_height - 50, 200, 50))
        player.draw(screen)  # Use Player's draw method

        # Drawing movable objects
        for obj in objects:
            obj.draw(screen)
        
        # Draw bullets
        for bullet in bullets:
            pygame.draw.circle(screen, white, bullet.center, 5)

        # Cap the frame rate
        pygame.time.Clock().tick(60)

        # Update the display
        pygame.display.flip()

