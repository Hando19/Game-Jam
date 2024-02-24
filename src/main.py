import pygame

#from screens.intro import intro_screen
#from screens.house_cleaning import mouse_infestation_screen
#from HouseCleaning.house import house_level
#from TakingTrashOut.trash import trash_level
from EliminatingPests.pest import pest_level
#from screens.end import end_screen

def main(): 
    # Initialize Pygame
    pygame.init()

    # Title
    pygame.display.set_caption("Chores")

    try:
        #mouse_infestation_screen()
        #house_level()
        #trash_level()
        pest_level()
        #end_screen()
    finally:
        pygame.quit()
    
if __name__ == "__main__":
    main()

