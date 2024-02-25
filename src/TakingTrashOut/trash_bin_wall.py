from setup.game_setup import wall_dimentions, screen_height
from classes.houseSprites import HouseSprites
from setup.util_functions import create_wall

bin_walls = [ 
    create_wall(200, screen_height - wall_dimentions, 200, wall_dimentions)
]

def draw_bins(screen):
    house_sprites = HouseSprites()

    for index, wall in enumerate(bin_walls):
        if index == 0:
            wall_sprite = house_sprites.get_trash_bin()
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
