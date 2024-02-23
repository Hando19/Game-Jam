import pygame
from setup.game_setup import screen_width, screen_height

# Function to create walls
def create_wall(x, y, width, height):
    """Creates a wall with the given parameters and returns the rect."""
    return pygame.Rect(x, y, width, height)

# Wall width/height
wall_height = 50

# Create walls
walls = [ 
    # Top wall
    create_wall(0, 0, screen_width, wall_height), 

    # Bottom wall
    create_wall(0, screen_height - wall_height, screen_width, wall_height),  

    # Left wall
    create_wall(0, 0, wall_height, screen_height),  
    
    #right wall from starting area
    create_wall(125, 50, wall_height, 200), 

    #bottom block from starting area
    create_wall(50, 325, 200, wall_height),

    create_wall(125, 450, wall_height, 150),

    #downward facing c 
    create_wall(250, 115, wall_height, 260),
    create_wall(250, 115, 200, wall_height),
    create_wall(450, 115, wall_height, 150),

    #exist corner
    create_wall(600, 115, 125, wall_height, ),
    create_wall(600, 50, wall_height, 75, )

]