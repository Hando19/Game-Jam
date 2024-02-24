import pygame
from setup.game_setup import screen_height, screen_width, wall_dimentions
from classes.houseSprites import HouseSprites
from classes.animalSprites import AnimalSprites

# Function to create walls
def create_wall(x, y, width, height):
    """Creates a wall with the given parameters and returns the rect."""
    return pygame.Rect(x, y, width, height)

# Create walls
walls = [ 

    #right wall from starting area
    create_wall(125, 10, wall_dimentions, 250), 

    #bottom block from starting area
    create_wall(10, 325, 250, wall_dimentions),

    #bottom left wall by coin
    create_wall(125, 450, wall_dimentions, 150),

    #downward facing c 
    create_wall(250, 115, wall_dimentions, 350),
    create_wall(450, 115, wall_dimentions, 150),
    create_wall(250, 107, 250, wall_dimentions),

    #exist corner
    create_wall(600, 115, 100, wall_dimentions),
    create_wall(600, 50, wall_dimentions, 400),

    #middle ish coin corner
    create_wall(400, 330, wall_dimentions, 150),
    create_wall(400, 325, 200, wall_dimentions),

    # Top wall
    create_wall(0, 0, screen_width, wall_dimentions), 

    # Bottom wall
    create_wall(0, screen_height - wall_dimentions, screen_width, wall_dimentions),  

    # Left wall
    create_wall(0, 0, wall_dimentions, screen_height),

    # Right wall
    create_wall(screen_width - wall_dimentions, 0, wall_dimentions, screen_height)
]

def draw_walls(screen):
    house_sprites = HouseSprites()

    for index, wall in enumerate(walls):
        # Determine which sprite to use based on the wall's index or other criteria
        if index == 0 or index == 2 or index == 3 or index == 4 or index == 7 or index == 8:
            wall_sprite = house_sprites.get_horizontal_inner_wall()
        elif index == 1 or index == 5 or index == 6 or index == 9:
            wall_sprite = house_sprites.get_vertical_inner_wall()
        elif index == len(walls)-4:
            wall_sprite = house_sprites.get_bottom_roof()
        elif index == len(walls)-3:
            wall_sprite = house_sprites.get_upper_roof()
        elif index == len(walls)-2:
            wall_sprite = house_sprites.get_right_roof()
        elif index == len(walls)-1:
            wall_sprite = house_sprites.get_left_roof()
        else:
            wall_sprite = house_sprites.get_floor()
        
        # Draw the selected sprite on the wall
        num_sprites_horizontal = wall.width // 50
        num_sprites_vertical = wall.height // 50
        
        for i in range(num_sprites_horizontal):
            for j in range(num_sprites_vertical):
                sprite_x = wall.x + i * 50
                sprite_y = wall.y + j * 50
                screen.blit(wall_sprite, (sprite_x, sprite_y))
