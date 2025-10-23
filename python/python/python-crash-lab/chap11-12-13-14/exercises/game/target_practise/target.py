import pygame


class Target:
    """A class to manage the Target."""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.visble = True


        self.image = pygame.image.load('target_practise/images/rectangle.png')
        self.rect = self.image.get_rect()



        self.rect.right = self.screen_rect.right - 50
        self.rect.centery = self.screen_rect.centery

    
        self.y = float(self.rect.y)
        

    
    def update(self):
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y
        self.change_direction()

    def change_direction(self):
        if self.rect.bottom >= self.screen_rect.bottom:
            self.settings.target_direction *= -1
        elif self.rect.top <= 0:
            self.settings.target_direction *=  -1

    def blitme(self):
        """Draw the ship at its current location."""
        if self.visble:
            self.screen.blit(self.image, self.rect)

        


