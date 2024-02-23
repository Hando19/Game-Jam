import pygame

from setup.game_setup import white, black, screen_height, screen_width, screen

def end_screen():
    # Initialize font
    font = pygame.font.SysFont(None, 48)

    # Ending messages
    game_over_message = "Game Over"
    thanks_message = "Thanks for playing!"
    game_over_text = font.render(game_over_message, True, white)
    thanks_text = font.render(thanks_message, True, white)
    game_over_text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    thanks_text_rect = thanks_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False  # Exit the loop if any key is pressed

        # Fill the screen with black
        screen.fill(black)

        # Draw the ending messages
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(thanks_text, thanks_text_rect)

        # Update the display
        pygame.display.flip()
