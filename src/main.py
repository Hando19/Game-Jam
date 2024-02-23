import pygame
import sys

from Laundry.laundry import laundry_level
from TakingTrashOut.trash import trash_level

def main():
    # Manually setting maze to starting level
    level_start = "trash" 
    
    if level_start == "laundry":
        laundry_level()
    elif level_start == "trash":
        trash_level()
    else:
        print("error")
    '''
    else level_start == "pests":
        laundry_level()
    '''
if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Title
    pygame.display.set_caption("Platform Game")

    main()
    pygame.quit()
    sys.exit()
