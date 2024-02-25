import pygame
import sys
from setup.game_setup import white, black, screen_height, screen_width, screen

def trash_removal_screen():
    # Initialize font
    font_big = pygame.font.SysFont(None, 64)
    font_small = pygame.font.SysFont(None, 48)

    # Messages
    title_message = "Get rid of the bears!"
    instruction_message = "Move the trash bags into the bins."

    # Render messages
    title_text = font_big.render(title_message, True, white)
    instruction_text = font_small.render(instruction_message, True, white)

    # Position messages
    title_text_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    instruction_text_rect = instruction_text.get_rect(center=(screen_width // 2, screen_height // 2 + 20))

    # Display time
    display_time_ms = 5000  # Show screen for 5000 milliseconds (5 seconds)
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
        screen.blit(title_text, title_text_rect)
        screen.blit(instruction_text, instruction_text_rect)

        # Update the display
        pygame.display.flip()
