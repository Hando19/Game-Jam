import pygame
import sys
from setup.game_setup import white, black, screen_height, screen_width, screen

def insect_destruction_screen():
    # Initialize font
    font_big = pygame.font.SysFont(None, 64)
    font_small = pygame.font.SysFont(None, 48)

    # Messages
    title_message = "Destroy all insect nests."
    instruction_message_1 = "Avoid the insects."
    instruction_message_2 = "Use space to blast insects to destroy nests?"

    # Render messages
    title_text = font_big.render(title_message, True, white)
    instruction_text_1 = font_small.render(instruction_message_1, True, white)
    instruction_text_2 = font_small.render(instruction_message_2, True, white)

    # Position messages
    title_text_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 80))
    instruction_text_1_rect = instruction_text_1.get_rect(center=(screen_width // 2, screen_height // 2))
    instruction_text_2_rect = instruction_text_2.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

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
        screen.blit(instruction_text_1, instruction_text_1_rect)
        screen.blit(instruction_text_2, instruction_text_2_rect)

        # Update the display
        pygame.display.flip()
