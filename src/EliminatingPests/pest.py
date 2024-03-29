import pygame
import random
from setup.game_setup import screen_height, screen_width, screen
from setup.util_functions import prepare_background
from classes.animalSprites import AnimalSprites
from classes.houseSprites import HouseSprites
from setup.player import Player  
from classes.projectile import Projectile

# Bullet properties
bullet_speed = 2
bullet_radius = 4
enemy_bullet_speed = 10
MAX_ENEMY_BULLETS = 10
player = Player()
animal_sprites = AnimalSprites()
house_sprites = HouseSprites()

# Initialize game entities and state
def init_game(player):
    global objects, player_bullets, enemy_bullets, collision_count
    objects = [pygame.Rect(random.randint(0, screen_width - 50), random.randint(0, screen_height - 50), 50, 50) for _ in range(random.randint(1, 5))]
    player_bullets = []
    enemy_bullets = []
    collision_count = 0

def add_player_bullet(player):
    player_bullets.append(Projectile((player.get_hitbox_rect().right, player.get_hitbox_rect().centery), "right", bullet_speed, screen_width))

def add_enemy_bullet():
    if len(enemy_bullets) >= MAX_ENEMY_BULLETS:
        return  # Exit if the maximum number of bullets is reached

    spawn_edge = random.choice(['top', 'right', 'bottom', 'left'])
    if spawn_edge == 'top':
        x = random.randint(0, screen_width)
        y = 0
        direction = "down" 
    elif spawn_edge == 'right':
        x = screen_width
        y = random.randint(0, screen_height)
        direction = "left"
    elif spawn_edge == 'bottom':
        x = random.randint(0, screen_width)
        y = screen_height
        direction = "up"
    elif spawn_edge == 'left':
        x = 0
        y = random.randint(0, screen_height)
        direction = "right"

    # Adjust speed and range based on direction if needed
    speed = enemy_bullet_speed  # You can also randomize this if you want
    range = max(screen_width, screen_height)  # Simple way to ensure bullet travels full distance

    # Create a new bullet and add it to the list
    new_bullet = Projectile((x, y), direction, speed, range)
    enemy_bullets.append(new_bullet)

def pest_level():
    global player, player_bullets, enemy_bullets, objects  # Ensure these are accessible globally
    init_game(player)
    
    running = True
    player_bullet_timer = 0
    enemy_bullet_timer = 0
    bullet_interval = 110
    enemy_bullet_interval = 30

    # Preparing background using single sprite
    background = pygame.Surface((screen_width, screen_height))
    background = prepare_background(background, house_sprites.get_grass())

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        proposed_move = player.propose_move()

        # Update player position if not colliding with objects
        if not any(proposed_move.colliderect(obj) for obj in objects):
            player.update_hitbox_rect(proposed_move)

        # Check for collisions between player and nests
        for obj in list(objects):  # Iterate over a copy of the list to safely remove items
            if player.get_hitbox_rect().colliderect(obj):
                objects.remove(obj)  # Remove the nest from the list

        # Check if all nests are collected
        if not objects:

            running = False  # Or transition to the next level or state

        # Player shooting bullets
        if keys[pygame.K_SPACE] and player_bullet_timer >= bullet_interval:
            add_player_bullet(player)
            player_bullet_timer = 0

        # Enemy shooting bullets
        if enemy_bullet_timer >= enemy_bullet_interval:
            add_enemy_bullet()
            enemy_bullet_timer = 0

        player_bullet_timer += 1
        enemy_bullet_timer += 1

        # Blit the background surface to the screen at the start of each frame
        screen.blit(background, (0, 0))
        
        for bullet in player_bullets + enemy_bullets:
            bullet.update()
            bullet.draw_insect(screen)
            if bullet in enemy_bullets and bullet.rect.colliderect(player.get_hitbox_rect()):
                init_game(player)  # Reset the game if the player is hit
                break
        
        # Update and draw player bullets, check for collisions with nests
        for bullet in player_bullets[:]:
            bullet.update()
            bullet.draw_insect(screen)
            for obj in objects[:]:
                if bullet.rect.colliderect(obj):
                    player_bullets.remove(bullet)
                    objects.remove(obj)
                    break

        # Check if all nests are hit
        if not objects:
            running = False
        
        # Draw nests
        for obj in objects:
            screen.blit(animal_sprites.get_insect_nest(), obj.topleft)

        player.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)
