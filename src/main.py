import pygame
import sys

from Laundry.laundry import laundry_level
from TakingTrashOut.trash import trash_level
from EliminatingPests.pest import pest_level
from screens.end import end_screen

def main():
    # Initialize Pygame
    pygame.init()

    # Title
    pygame.display.set_caption("Platform Game")

    try:
        pest_level()
        end_screen()
    finally:
        pygame.quit()
    
if __name__ == "__main__":
    main()

