import pygame

class AlienBoss:
    """Initializing the alien boss"""
    def __init__(self, ai_game):
        
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.shoot_cooldown = 0
        self.can_shoot = False
        self.boss_health = 7

      

        self.image = pygame.image.load("Alien_invasion/images/boze.png")
        self.rect = self.image.get_rect()

        self.rect.midtop = self.screen_rect.midtop

    

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        self.x += self.settings.alien_boss_speed * self.settings.fleet_direction
        self.rect.x = self.x

        if self.can_shoot:
            if self.shoot_cooldown > 0:
                self.shoot_cooldown -= 1
            else:
                self.ai_game._fire_bullet_boss()
                self.shoot_cooldown = 30


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midtop  = self.screen_rect.midtop
        self.x = float(self.rect.x)

     