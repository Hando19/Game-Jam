import pygame

# Screen dimensions
screen_width = 800
screen_height = 600

# A 1x1 wall would be 50 x 50
wall_dimentions = 50

projectile_dimentions = 20

broom_dimensions = 30

nest_dimensions = 40
trashbin_dimensions = 10

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100) 
red = (255, 0, 0)
yellow = (255, 255, 0)  
dark_gray = (50, 50, 50)
light_purple = (200, 160, 255)

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))
