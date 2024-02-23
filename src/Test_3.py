import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 800

# Colors
black = (0, 0, 0)
white = (255, 255, 255)  # Color for random bullets
red = (255, 0, 0)  # Color for movable objects
yellow = (255, 255, 0)  # Color for player bullets
grey = (50, 50, 50)

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Mischievous Mansion")

# Floor properties
floor_height = 50  # Height of the floor area
floor_color = grey
floor_rect = pygame.Rect(0, screen_height - floor_height, screen_width, floor_height)

# Initialize game entities and state
def init_game():
    global player_rect, objects, player_bullets, enemy_bullets, collision_count
    # Player always spawns in the top left corner
    player_rect = pygame.Rect(0, 0, 50, 50)
    # Random number of red blocks
    num_blocks = random.randint(1, 5)  # Generate between 1 and 5 blocks
    # Reset objects to random positions away from the player
    objects = []
    for _ in range(num_blocks):
        while True:
            spawn_radius = 300
            x = random.randint(spawn_radius, screen_width - spawn_radius)
            y = random.randint(spawn_radius, screen_height - spawn_radius)
            obj_rect = pygame.Rect(x, y, 50, 50)
            # Check collision with player and other objects
            if not obj_rect.colliderect(player_rect) and not any(obj_rect.colliderect(obj) for obj in objects):
                objects.append(obj_rect)
                break
    player_bullets = []  # List to hold player bullets
    enemy_bullets = []  # List to hold enemy bullets
    collision_count = 0  # Reset collision counter

init_game()

# Load Player Sprite
player_image = pygame.Surface((50, 50))  # Placeholder for player sprite
player_image.fill(white)

# Player properties
player_speed = 5

# Bullet properties
bullet_speed = 2
bullet_radius = 4
enemy_bullet_speed = 10

# Initialize Pygame font
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Function to add player bullets
def add_player_bullet():
    y = player_rect.centery  # Bullet spawns at the center of the player vertically
    bullet_rect = pygame.Rect(player_rect.right, y, bullet_radius * 1, bullet_radius * 1)
    player_bullets.append(bullet_rect)

# Function to add enemy bullets
def add_enemy_bullet():
    # Spawn enemy bullets from the top
    x_top = random.randint(0, screen_width - 1)
    bullet_rect_top = pygame.Rect(x_top, 0, bullet_radius * 2, bullet_radius * 2)
    bullet_velocity_top = [0, enemy_bullet_speed]  # Move downwards
    enemy_bullets.append((bullet_rect_top, bullet_velocity_top))

    # Spawn enemy bullets from the right
    y_right = random.randint(0, screen_height - 1)
    bullet_rect_right = pygame.Rect(screen_width, y_right, bullet_radius * 2, bullet_radius * 2)
    bullet_velocity_right = [-enemy_bullet_speed, 0]  # Move leftwards
    enemy_bullets.append((bullet_rect_right, bullet_velocity_right))

# Game loop flag
running = True
player_bullet_timer = 0
enemy_bullet_timer = 0
bullet_interval = 110  # Frames until a new bullet is added
enemy_bullet_interval = 30  # Frames until a new enemy bullet is added

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    # Check for player bullet spawning (spacebar pressed)
    if keys[pygame.K_SPACE]:
        # Add a new player bullet if enough time has passed
        if player_bullet_timer >= bullet_interval:
            add_player_bullet()
            player_bullet_timer = 0

    # Check for enemy bullet spawning
    if enemy_bullet_timer >= enemy_bullet_interval:
        add_enemy_bullet()
        enemy_bullet_timer = 0

    # Increment bullet timers
    player_bullet_timer += 1
    enemy_bullet_timer += 1

    # Update player bullets
    for bullet in player_bullets[:]:
        bullet.x += bullet_speed
        if bullet.x > screen_width:
            player_bullets.remove(bullet)
        # Check collision with objects
        for obj in objects[:]:
            if bullet.colliderect(obj):
                player_bullets.remove(bullet)
                objects.remove(obj)
                collision_count += 1  # Update the counter when a red block disappears

    # Update enemy bullets
    for bullet, velocity in enemy_bullets[:]:
        bullet.x += velocity[0]  # Update x-coordinate
        bullet.y += velocity[1]  # Update y-coordinate
        if bullet.x < 0 or bullet.y > screen_height:
            enemy_bullets.remove((bullet, velocity))
        # Check collision with player
        if bullet.colliderect(player_rect):
            init_game()  # Reset game if player is hit

    # Fill the screen with black
    screen.fill(black)

    # Draw the floor
    pygame.draw.rect(screen, floor_color, floor_rect)

    # Draw the player
    screen.blit(player_image, player_rect.topleft)

    # Draw movable objects
    for obj in objects:
        pygame.draw.rect(screen, red, obj)

    # Render the collision counter
    counter_text = font.render(f"Disappeared Blocks: {collision_count}", True, white)
    screen.blit(counter_text, (10, 10))

    # Draw player bullets
    for bullet in player_bullets:
        pygame.draw.circle(screen, yellow, bullet.center, bullet_radius)

    # Draw enemy bullets
    for bullet, _ in enemy_bullets:
        pygame.draw.circle(screen, white, bullet.center, bullet_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
