import pygame

# Function to create walls
def create_wall(x, y, width, height):
    """Creates a wall with the given parameters and returns the rect."""
    return pygame.Rect(x, y, width, height)

# A 1x1 wall would be 50 x 50
wall_dimentions = 50

# Create walls
walls = [ 
    # Top wall
    create_wall(0, 0, 800, wall_dimentions), 

    # Bottom wall
    create_wall(0, 600 - wall_dimentions, 800, wall_dimentions),  

    # Left wall
    create_wall(0, 0, wall_dimentions, 600),

    # Right wall
    create_wall(800 - wall_dimentions, 0, wall_dimentions, 600),  
    
    #right wall from starting area
    create_wall(125, 50, wall_dimentions, 200), 

    #bottom block from starting area
    create_wall(50, 325, 200, wall_dimentions),

    create_wall(125, 450, wall_dimentions, 150),

    #downward facing c 
    create_wall(250, 115, wall_dimentions, 370),
    create_wall(250, 115, 200, wall_dimentions),
    create_wall(450, 115, wall_dimentions, 150),

    #exist corner
    create_wall(600, 115, 90, wall_dimentions, ),
    create_wall(600, 50, wall_dimentions, 400, ),

    create_wall(400, 325, 200, wall_dimentions),

    create_wall(400, 340, wall_dimentions, 150)
]