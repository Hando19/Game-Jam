import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
light_purple = (200, 160, 255)

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Start Game")

# Initialize font
font = pygame.font.SysFont(None, 48)

# Start button properties
button_width = 100
button_height = 100
button_color = light_purple
button_text = "Start"
button_text_color = black

# Calculate button position
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2

# Additional text properties
additional_text = "Here is our interpretation of doing messy house chores"
additional_text_color = white
additional_text_font = pygame.font.SysFont(None, 24)

# Calculate additional text position
additional_text_x = -additional_text_font.size(additional_text)[0]
additional_text_y = button_y + button_height + 20
additional_text_speed = 3  # Adjust the speed of the text movement

# Function to check if a point is inside the button rectangle
def is_inside_button(pos):
    return button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if is_inside_button(mouse_pos):
                subprocess.run(["python", "Level2.py"])  # Run Level2.py script

    # Update the position of the additional text
    additional_text_x += additional_text_speed
    if additional_text_x > screen_width:
        additional_text_x = -additional_text_font.size(additional_text)[0]

    # Fill the screen with black
    screen.fill(black)

    # Draw the button
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    button_text_surface = font.render(button_text, True, button_text_color)
    button_text_rect = button_text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(button_text_surface, button_text_rect)

    # Draw the additional text
    additional_text_surface = additional_text_font.render(additional_text, True, additional_text_color)
    screen.blit(additional_text_surface, (additional_text_x, additional_text_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
