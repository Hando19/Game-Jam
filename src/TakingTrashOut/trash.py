import pygame
import sys
import random

from setup.game_setup import black, white, gray, red, dark_gray, screen_height, screen_width, screen
from setup.player import player_image, player_speed

# Initialize game entities and state
def init_game():
    global player_rect, objects, bullets, collision_count
    
    # Player always spawns in the top left corner
    player_rect = pygame.Rect(0, 0, 50, 50)
    # Reset objects to random positions away from the player
    objects = []
    num_objects = random.randint(3, 6)  # Random number of objects between 3 and 6
    for _ in range(num_objects):  # Random objects
        while True:
            obj_rect = pygame.Rect(random.randint(100, screen_width - 100), random.randint(100, screen_height - 100), 50, 50)
            if not obj_rect.colliderect(player_rect):
                objects.append(obj_rect)
                break
    bullets = []  # List to hold bullets
    collision_count = 0  # Reset collision counter

# Initialize Pygame font
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Function to add bullets
def add_bullet():
    y = random.randint(0, screen_height)
    bullet_rect = pygame.Rect(screen_width, y, 10, 10)
    bullets.append(bullet_rect)

def trash_level():
    global collision_count

    init_game()

    # Bullet properties
    bullet_speed = 12

    # Floor properties
    floor_height = 50  # Height of the floor area
    floor_color = gray
    floor_rect = pygame.Rect(0, screen_height - floor_height, screen_width, floor_height)

    # Pit properties
    pit_rect = pygame.Rect(200, screen_height - floor_height, 200, floor_height)  # Example pit position and size

    # Pit hitbox properties (slightly above the pit, same length)
    pit_hitbox_rect = pygame.Rect(pit_rect.x, pit_rect.y - 10, pit_rect.width, 10)  # 10 pixels high hitbox above the pit

    # Game loop flag
    running = True
    bullet_timer = 0
    bullet_interval = 60  # Frames until a new bullet is added

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Key press handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed
        if keys[pygame.K_UP]:
            player_rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            player_rect.y += player_speed

        # Ensure player remains on screen
        player_rect.x = max(0, min(screen_width - player_rect.width, player_rect.x))
        player_rect.y = max(0, min(screen_height - floor_height - player_rect.height, player_rect.y))

        # Check for collisions and move objects if collided with the player
        for obj in objects[:]:
            if player_rect.colliderect(obj):
                if keys[pygame.K_LEFT] and obj.x > 0:
                    obj.x -= player_speed
                if keys[pygame.K_RIGHT] and obj.x < screen_width - obj.width:
                    obj.x += player_speed
                if keys[pygame.K_UP] and obj.y > 0:
                    obj.y -= player_speed
                if keys[pygame.K_DOWN] and obj.y < screen_height - floor_height - obj.height:
                    obj.y += player_speed
                
                # Check if the object is in the pit hitbox and remove it
                if pit_hitbox_rect.colliderect(obj):
                    objects.remove(obj)  # Remove the object if it's in the hitbox above the pit
                    collision_count += 1  # Update the counter when a red block disappears

        # Bullet logic
        bullet_timer += 1
        if bullet_timer >= bullet_interval:
            add_bullet()
            bullet_timer = 0
        
        # Update bullets
        for bullet in bullets[:]:
            bullet.x -= bullet_speed
            if bullet.x < 0:
                bullets.remove(bullet)
            # Check collision with player
            if bullet.colliderect(player_rect):
                init_game()  # Reset game if player is hit

        # Fill the screen with black
        screen.fill(black)

        # Draw the floor
        pygame.draw.rect(screen, floor_color, floor_rect)

        # Draw the pit
        pygame.draw.rect(screen, dark_gray, pit_rect)

        # Draw the player
        screen.blit(player_image, player_rect.topleft)

        # Draw movable objects
        for obj in objects:
            pygame.draw.rect(screen, red, obj)

        # Render the collision counter
        counter_text = font.render(f"Disappeared Blocks: {collision_count}", True, white)
        screen.blit(counter_text, (10, 10))

        # Update bullets
        for bullet in bullets:
            pygame.draw.circle(screen, white, bullet.center, 5)

        # Cap the frame rate
        pygame.time.Clock().tick(60)

        # Update the display
        pygame.display.flip()

