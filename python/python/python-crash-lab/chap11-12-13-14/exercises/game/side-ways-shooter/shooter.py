import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import  random
from game_stats import GameStats
from time import sleep


class Shooter:
    """Shooter Enxtension"""
    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Shooter spree Invasion")

        self.game_active = True
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.update_aliens()
            self._update_screen()
            self.clock.tick(60)



    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    

    def _fire_bullet(self):
        if len(self.bullet)  < self.settings.bullet_allowed:
            new_bullets = Bullet(self)
            self.bullet.add(new_bullets)

    
    def _update_bullets(self): 
        self.bullet.update()
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)
        self._check_bullet_alien_collisions()
    
    
    def _check_bullet_alien_collisions(self):
         """Respond to bullet-alien collisions."""
         # Remove any bullets and aliens that have collided.
         collisions = pygame.sprite.groupcollide(self.bullet, self.aliens, True, True)
         if not self.aliens: 
                   # Destroy existing bullet and create new fleet.
                   self.bullet.empty()
                   self._create_fleet()
                   

        
    def _create_fleet(self):
         """Create the fleet of aliens."""
         # Make an alien and keep adding aliens until there is no room left
         # Spacing between aliens is one alien width and one alien height
         alien = Alien(self)
         alien_width, alien_height = alien.rect.size

         current_x, current_y = alien_width, alien_height
         while current_y < (self.settings.screen_height - (3 * alien_height)):
            while current_x < (self.settings.screen_width - (2 * alien_width)):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_positon):
         """Create an alien and place it in the row."""
         new_alien = Alien(self)
         new_alien.x = x_position
         new_alien.rect.x = x_position
         new_alien.rect.y = y_positon
         scale = random.randint(4,6)
         if scale == 5:   
           self.aliens.add(new_alien)
  
    def _check_fleet_edges(self):
         """Respond appropriately if any aliens have reached an edge"""
         for alien in self.aliens.sprites():
              if alien.check_edges():
                   self._change_fleet_direction()
                   break

    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleet's direction."""
         for alien in self.aliens.sprites():
              alien.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1
    

    def update_aliens(self):
         """Update the positions of all aliens in the fleet."""
         self._check_fleet_edges()
         self.aliens.update()

         if pygame.sprite.spritecollideany(self.ship, self.aliens):
             self.ship_hit()

         self._check_alien_bottom()
    
    def ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1

            self.bullet.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(1.0)

        else:
            self.game_active = False


    def _check_alien_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self.ship_hit()
                break

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullet.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    sht = Shooter()
    sht.run_game()