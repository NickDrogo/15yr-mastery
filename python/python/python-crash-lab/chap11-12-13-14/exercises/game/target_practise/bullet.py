import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """Create a bullet objects at the ship's current position."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct poition.
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = ai_game.ship.rect.midleft

        #Store the bullet's position as a float

        self.x = float(self.rect.x)
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.x += self.settings.bullet_speed
        # update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect) 
