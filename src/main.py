import pygame
import sys

from maze.maze_level import maze_level

def main():
    # Manually setting maze to starting level
    level_start = "maze" 
    
    if level_start == "maze":
        maze_level()
    # elif level_start == "another_level":
    #     another_level()
    # Add more levels as needed

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Title
    pygame.display.set_caption("Platform Game")

    main()
    pygame.quit()
    sys.exit()
