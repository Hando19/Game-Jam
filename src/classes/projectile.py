import pygame
from setup.game_setup import red, projectile_dimentions
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
    
    def draw(self, surface):
        animal_sprites = AnimalSprites()

        # Draw the projectile
        pygame.draw.rect(surface, self.color, self.rect)
        
        # Overlay the specific image
        if self.direction == "right":
            image = animal_sprites.get_mouse_right_face()
        elif self.direction == "left":
            image = animal_sprites.get_mouse_left_face()
        elif self.direction == "up":
            image = animal_sprites.get_mouse_upward_face()
        elif self.direction == "down":
            image = animal_sprites.get_mouse_downward_face()
        
        # Draw the image on top of the projectile
        surface.blit(image, self.rect.topleft)