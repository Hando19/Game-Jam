import pygame
from setup.util_functions import get_sprite

class Player:
    def __init__(self):
        # Load Player Sprite
        self.player_image_path = 'src/assets/PlayerAssets.png'
        self.player_image = get_sprite(self.player_image_path, 1.5, 1.5, 60, 35, 50).convert_alpha()
        self.player_rect = self.player_image.get_rect(topleft=(75, 75))
        self.hitbox_padding = 10
        # Adjust the player_rect to create a tighter hitbox around the visible sprite
        self.hitbox_rect = self.player_rect.inflate(-self.hitbox_padding * 2, 0)

        # Player properties
        self.player_speed = 5

    def propose_move(self):
        proposed_rect = self.get_hitbox_rect().copy()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            proposed_rect.x -= self.player_speed
        if keys[pygame.K_RIGHT]:
            proposed_rect.x += self.player_speed
        if keys[pygame.K_UP]:
            proposed_rect.y -= self.player_speed
        if keys[pygame.K_DOWN]:
            proposed_rect.y += self.player_speed
        return proposed_rect

    def update_spawn_position(self, spawn_cords):
        self.hitbox_rect.topleft = spawn_cords
    
    def update_hitbox_rect(self, new_rect):
        self.hitbox_rect = new_rect

    def get_hitbox_rect(self):
        return self.hitbox_rect
    
    def draw(self, surface):
        image_x = self.hitbox_rect.x - self.hitbox_padding
        image_y = self.hitbox_rect.y
        surface.blit(self.player_image, (image_x, image_y))