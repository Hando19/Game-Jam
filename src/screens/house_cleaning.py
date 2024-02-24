import pygame
import sys
from setup.game_setup import white, black, screen_height, screen_width, screen

def mouse_infestation_screen():
    # Initialize font
    font_big = pygame.font.SysFont(None, 64)
    font_small = pygame.font.SysFont(None, 48)

    # Messages
    infestation_message = "You have a mouse infestation!"
    action_message = "Collect the brooms to clear them out."

    # Render messages
    infestation_text = font_big.render(infestation_message, True, white)
    action_text = font_small.render(action_message, True, white)

    # Position messages
    infestation_text_rect = infestation_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    action_text_rect = action_text.get_rect(center=(screen_width // 2, screen_height // 2 + 20))

    # Display time
    display_time_ms = 5000 
    start_ticks = pygame.time.get_ticks()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Calculate elapsed time
        elapsed_time_ms = pygame.time.get_ticks() - start_ticks
        if elapsed_time_ms >= display_time_ms:
            running = False

        # Fill the screen with black
        screen.fill(black)

        # Draw the messages
        screen.blit(infestation_text, infestation_text_rect)
        screen.blit(action_text, action_text_rect)

        # Update the display
        pygame.display.flip()
