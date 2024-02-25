import pygame

from screens.intro import intro_screen
from screens.house_cleaning import mouse_infestation_screen
from HouseCleaning.house import house_level
from screens.trash_removal import trash_removal_screen
from TakingTrashOut.trash import trash_level
from screens.pest_extermination import insect_destruction_screen
from EliminatingPests.pest import pest_level
from screens.end import end_screen
#The game is run on pygame. You have to make sure you have both
# Pygame and Python installed inorder to run the game.
def main(): 
    # Initialize Pygame
    pygame.init()

    # Title
    pygame.display.set_caption("Mr.Clean Fights Back")

    try:
        intro_screen()
        mouse_infestation_screen()
        house_level()
        trash_removal_screen()
        trash_level()
        insect_destruction_screen()
        pest_level()
        end_screen()
    finally:
        pygame.quit()
    
if __name__ == "__main__":
    main()

