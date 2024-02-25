import pygame
from setup.game_setup import projectile_dimentions
from classes.animalSprites import AnimalSprites

class Projectile:
    def __init__(self, start_pos, direction, speed, range):
        self.original_start_pos = start_pos  # Save the original start position
        self.rect = pygame.Rect(start_pos[0], start_pos[1], projectile_dimentions, projectile_dimentions)
        self.direction = direction
        self.speed = speed
        self.start_pos = start_pos
        self.range = range
        self.color = (0, 0, 0, 0)
        self.distance_moved = 0  # Track how far the projectile has moved
        self.animal_sprites = AnimalSprites()
    
    def update(self):
        """Move the projectile and reset it if it exceeds its range."""
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        
        # Calculate the distance moved
        dx = self.rect.x - self.original_start_pos[0]
        dy = self.rect.y - self.original_start_pos[1]
        self.distance_moved = (dx**2 + dy**2)**0.5
        
        # Reset the projectile if it has exceeded its range
        if self.distance_moved > self.range:
            self.reset()
    
    def reset(self):
        """Reset the projectile to its original position."""
        self.rect.x, self.rect.y = self.original_start_pos
        self.distance_moved = 0
    
    def draw_insect(self, surface):

        # Get the specific image based on direction
        if self.direction == "right":
            image = self.animal_sprites.get_insect_right_face()
        elif self.direction == "left":
            image = self.animal_sprites.get_insect_left_face()
        elif self.direction == "up":
            image = self.animal_sprites.get_insect_upward_face()
        elif self.direction == "down":
            image = self.animal_sprites.get_insect_downward_face()
        
        surface.blit(image, self.rect.topleft)

    def draw_mice(self, surface):

        # Get the specific image based on direction
        if self.direction == "right":
            image = self.animal_sprites.get_mouse_right_face()
        elif self.direction == "left":
            image = self.animal_sprites.get_mouse_left_face()
        elif self.direction == "up":
            image = self.animal_sprites.get_mouse_upward_face()
        elif self.direction == "down":
            image = self.animal_sprites.get_mouse_downward_face()
        
        surface.blit(image, self.rect.topleft)
