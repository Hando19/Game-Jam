import pygame
import sys

def create_wall(x, y, width, height, color):
    """Creates a wall with the given parameters and returns the rect."""
    return pygame.Rect(x, y, width, height)

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)  # Color for the walls

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Platform Game")

# Create walls
wall_height = 50

top_wall = create_wall(0, 0, screen_width, wall_height, gray)
bottom_wall = create_wall(0, screen_height - wall_height, screen_width, wall_height, gray)
left_wall = create_wall(0, 0, wall_height, screen_height, gray)

walls = []  # Store wall rects here
walls.append(top_wall)
walls.append(bottom_wall)
walls.append(left_wall)

#right wall from starting area 
walls.append(create_wall(125, 50, wall_height, 200, gray))

#bottom block from starting area
walls.append(create_wall(50, 325, 200, wall_height, gray))

walls.append(create_wall(125, 450, wall_height, 150, gray))

#downward facing c 
walls.append(create_wall(250, 115, wall_height, 260, gray))
walls.append(create_wall(250, 115, 200, wall_height, gray))
walls.append(create_wall(450, 115, wall_height, 150, gray))

#exist corner
walls.append(create_wall(600, 115, 125, wall_height, gray))
walls.append(create_wall(600, 50, wall_height, 75, gray))

# Load Player Sprite
player_image = pygame.Surface((50, 50))  # Placeholder for player sprite
player_image.fill(white)

# Adjusted player spawn position
spawn_margin = 10  # Small margin to ensure player isn't overlapping or too close to a wall
player_size = 50  # Size of the player sprite

# Assuming the left_wall and top_wall are created earlier
spawn_x = left_wall.width + spawn_margin
spawn_y = top_wall.height + spawn_margin

# Update player_rect with the new spawn location
player_rect = player_image.get_rect(topleft=(spawn_x, spawn_y))

# Player properties
player_speed = 5

# Game loop flag
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

pygame.quit()
sys.exit()
