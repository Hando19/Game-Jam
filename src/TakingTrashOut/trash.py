import pygame
import sys
import random

from setup.game_setup import black, white, gray, red, dark_gray, screen_height, screen_width, screen, wall_dimentions

from setup.player import Player
from classes.movableObject import MovableObject
from HouseCleaning.projectile_manager import projectiles 
from classes.projectile import Projectile
from setup.util_functions import prepare_background
from classes.houseSprites import HouseSprites

# Initialize Pygame and font
pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Declare global variables
objects, bears, collision_count = [], [], 0
player = None  # This will be initialized in trash_level()

def init_game():
    global objects, bears, collision_count, player, background

    house_sprites = HouseSprites()
    # Preparing background using single sprite
    background = pygame.Surface((screen_width, screen_height))
    background = prepare_background(background, house_sprites.get_grass())

    player = Player()  # Reinitialize the player globally
    objects = []
    bears = []
    collision_count = 0
    num_objects = random.randint(3, 6)
    for _ in range(num_objects):
        x = random.randint(100, screen_width - 100)
        y = random.randint(100, screen_height - 100)
        new_object = MovableObject(x, y)
        while new_object.is_collided_with(player.get_hitbox_rect()):
            new_object.rect.x = random.randint(100, screen_width - 100)
            new_object.rect.y = random.randint(100, screen_height - 100)
        objects.append(new_object)

def add_bear():
    global projectiles, bears

    selected_projectile = random.choice(projectiles)
    
    # Determine the direction and set the starting position accordingly
    if selected_projectile.direction == "right":
        # Spawn on the left side, moving right
        start_pos = (0, random.randint(0, screen_height))
    elif selected_projectile.direction == "up":
        # Spawn at the bottom, moving up
        start_pos = (random.randint(0, screen_width), screen_height)
    else:
        # Default to spawning on the right side if direction is not "right" or "up"
        # This handles cases where the direction might not be explicitly set to "left" or "down"
        # Adjust this logic if you have specific needs for these directions
        start_pos = (screen_width, random.randint(0, screen_height))

    # Create a new Projectile with the adjusted starting position
    new_bear = Projectile(start_pos, selected_projectile.direction, selected_projectile.speed, selected_projectile.range)
    bears.append(new_bear)


def trash_level():
    global player, collision_count, background
    init_game()
    
    bear_speed = 12
    pit_rect = pygame.Rect(200, screen_height - wall_dimentions, 200, wall_dimentions)
    pit_hitbox_rect = pygame.Rect(pit_rect.x, pit_rect.y, pit_rect.width, 10)

    running = True
    bear_timer = 0
    bear_interval = 60

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        proposed_move = player.propose_move()

        proposed_move.x = max(0, min(screen_width - proposed_move.width, proposed_move.x))
        proposed_move.y = max(0, min(screen_height - proposed_move.height, proposed_move.y))

        player.update_hitbox_rect(proposed_move)

        for obj in list(objects):
            if proposed_move.colliderect(obj.rect):
                dx = dy = 0
                if keys[pygame.K_LEFT]: dx = -player.player_speed
                if keys[pygame.K_RIGHT]: dx = player.player_speed
                if keys[pygame.K_UP]: dy = -player.player_speed
                if keys[pygame.K_DOWN]: dy = player.player_speed

                obj.rect.x = max(0, min(screen_width - obj.rect.width, obj.rect.x + dx))
                obj.rect.y = max(0, min(screen_height - obj.rect.height, obj.rect.y + dy))

            if obj.rect.colliderect(pit_hitbox_rect):
                objects.remove(obj)
                collision_count += 1

        for bear in bears[:]:
            bear.update()
            if bear.distance_moved > bear.range or bear.rect.colliderect(pit_hitbox_rect):
                bears.remove(bear)
            elif bear.rect.colliderect(player.get_hitbox_rect()):
                init_game()  # Reset the game if the player is hit by a bear

        bear_timer += 1
        if bear_timer >= bear_interval:
            add_bear()
            bear_timer = 0

        # Draw the background first
        screen.blit(background, (0, 0))

        # Draw the rest of the game elements
        pygame.draw.rect(screen, dark_gray, (200, screen_height - 50, 200, 50))
        player.draw(screen)

        for obj in objects:
            obj.draw(screen)
        
        for bear in bears:
            bear.draw_bear(screen)

        # Display the score
        score_surface = font.render(f'Score: {collision_count}', True, pygame.Color('white'))
        screen.blit(score_surface, (10, 10))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == '__main__':
    trash_level()
