import sys
from ship import Ship
from settings import Settings
from bullet import Bullets
from alien import Alien
from game_stats import GameStat
from time import sleep
from buttons_play import ButtonsPlay
from button_hard import ButtonsHard
from button_medium import ButtonsMedium
from scoreboard import Scoreboard
from alien_boss import AlienBoss
from bullet_boss import BulletBoss



import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # , pygame.FULLSCREEN)
        pygame.display.set_caption("Alien Invasion")

               

        # Start Alien invasion in an active state.
        self.game_active = False

        # Make the button. 💡💡💡💡💡💡💡
        self.play_button = ButtonsPlay(self, "easy")
        self.hard_button = ButtonsHard(self, "Hard")
        self.medium_button = ButtonsMedium(self, "Medium")

        # Create an instance to store game statistics
        self.stats = GameStat(self)

        # Create an instance to store game statistics.
        # and create a scoreboard
        self.sb = Scoreboard(self)
        

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bulletboss = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alienboss = AlienBoss(self)
        
     
        self._create_fleet()
        self.shot = pygame.mixer.Sound("Alien_invasion/audio/shot.ogg")
        self.explosion = pygame.mixer.Sound("Alien_invasion/audio/explosion.ogg")

        #set the background color.
        # self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events() 
            if self.game_active:
               self.ship.update()
               self._update_bullets_ship()
               self._update_bullets_boss()
               self.update_aliens()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.reset_stats()
                sys.exit()  
            elif event.type == pygame.KEYDOWN:
                 self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)  

            elif event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
         """Start a new game when the player clicks Play."""
         buttonplay_clicked = self.play_button.rect.collidepoint(mouse_pos)
         buttonhard_clicked = self.hard_button.rect.collidepoint(mouse_pos)
         buttonmedium_clicked = self.medium_button.rect.collidepoint(mouse_pos)

         if buttonhard_clicked and not self.game_active:
                          # Reset the game statistics
                         self.settings.initialize_dynamic_settings_hard()
                         self._start_game() 
                    

         elif buttonmedium_clicked and not self.game_active:         
                         # Reset the game statistics
                         self.settings.initialize_dynamic_settings_medium()
                         self._start_game()  
                         

         elif buttonplay_clicked and not self.game_active:
                          # Reset the game statistics
                         self.settings.initialize_dynamic_settings_default()
                         self._start_game()
                         

    def _start_game(self):
          """Start game """
          self.stats.reset_stats()
          self.sb.prep_score()
          self.sb.prep_level()
          self.sb.prep_ships()
          self.sb.prep_high_score()
          
          self.game_active = True

          # Get rid of any remaining bullets and aliens.
          self.bullets.empty()
          self.aliens.empty()

          # Create a new fleet and center the ship.
          self._create_fleet()
          self.ship.center_ship()

          # Hide  the mouse cursor
          pygame.mouse.set_visible(False)


               
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
        # move the ship to the right.
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
              self.stats.reset_stats()
              sys.exit()

        elif event.key == pygame.K_SPACE:
             self._fire_bullet_ship()
             self.shot.play()
             self.ship.shield_active = False
          

        elif event.key == pygame.K_s:
              self.ship.shield_active = True
              

        elif event.key == pygame.K_p:
             self._start_game()
             

    def _check_keyup_events(self, event):
         """Respond to key releases"""    
         if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:   
                self.ship.moving_left = False
         elif event.key == pygame.K_s:
               self.ship.shield_active = False
     

    def _fire_bullet_ship(self):
         """Create a new bullet and add it to the bullets group."""
         if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)

    def _fire_bullet_boss(self):
          new_bullet = BulletBoss(self)
          self.bulletboss.add(new_bullet)

     
    def _update_bullets_ship(self):
         """Update position of bullets and get rid of old bullets."""
         # Update bullet positons
         # Get rid of bullets that have disappeared;
         self.bullets.update()

         for bullet in self.bullets.copy():
              if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
         self._check_bullet_alien_collisions()
         self._check_bullet_kill_boss_collisons()


    def _update_bullets_boss(self):
          self.bulletboss.update()
          for bullet in self.bulletboss.copy():
               if bullet.rect.bottom <= 0:
                    self.bulletboss.remove(bullet)
          self._check_bullet_boss_collisions() 


    def _start_new_level(self):
               self.alienboss.center_ship()
               self.alienboss.can_shoot = False
               # Destroy existing bullet and create new fleet.
               self.bullets.empty()
               self._create_fleet()
               self.settings.increase_speed()

               # Increase level
               self.stats.level += 1
               self.sb.prep_level()
               self._check_bullet_kill_boss_collisons()



    def _check_bullet_alien_collisions(self):
         """Respond to bullet-alien collisions."""
         # Remove any bullets and aliens that have collided.
         collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
         
         if collisions:
              for aliens in collisions.values():
                   self.stats.score += self.settings.alien_points * len(aliens)
              self.sb.prep_score()
              self.sb.check_high_score()
              if not self.aliens:
                    self.alienboss.can_shoot = True
     

    
    def _check_bullet_kill_boss_collisons(self):
          for bullet in self.bullets.sprites():
                if bullet.rect.colliderect(self.alienboss.rect):
                      bullet.kill()
                      if not self.aliens:
                           self.alienboss.boss_health -= 1
                           self.stats.score += self.settings.alien_points
                           self.sb.prep_score()
                           self.sb.check_high_score()
                         
                           if self.alienboss.boss_health <= 0:
                                 self.explosion.play()
                                 
                                 self._start_new_level()
                                 self.alienboss.boss_health = 7
                         
                              
    def _check_bullet_boss_collisions(self):
          for bullet in self.bulletboss.sprites():
                if self.ship.shield_active:
                      pass
                elif bullet.rect.colliderect(self.ship.rect):
                      self._ship_hit()
                      self.alienboss.can_shoot = False
               
          
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

              
    def _check_alien_boss_edges(self):
         """Respond appropriately  if alien boss have reached an edge"""
         if self.alienboss.check_edges():
               self._change_alien_boss_direction()
               
                    
    def _change_alien_boss_direction(self):
                    self.alienboss.rect.y += self.settings.alienboss_drop_speed
                    self.settings.fleet_direction *= -1

    def update_aliens(self):
         """Update the positions of all aliens in the fleet."""
         self._check_fleet_edges()
         self.aliens.update()
         self._check_alien_boss_edges()
         self.alienboss.update()

         # Look for alien-ship collisions.
         if pygame.sprite.spritecollideany(self.ship, self.aliens):
              self._ship_hit()
     
         # Look for aliens hitting the bottom of the screen.
         self.check_aliens_bottom()
         self.check_alien_boss_bottom()

    def _ship_hit(self):
         """respond to the ship being hit by an alien."""   
         if self.stats.ship_left > 0:     
               # Decrement ship_left and update scoreboard.
               self.stats.ship_left -= 1
               self.sb.prep_ships()

               # Get rid of any remaining bullets and aliens.
               self.bullets.empty()
               self.aliens.empty()

               # Create a new_fleet and ceter the ship.
               self._create_fleet()
               self.ship.center_ship()
               self.alienboss.center_ship()

               #Pause
               sleep(0.5)
         else:
              self.game_active = False
              pygame.mouse.set_visible(True)


    def check_aliens_bottom(self):
         """Check if any aliens have reached the bottom of the screen."""
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= self.settings.screen_height:
                   # Treat  this the same  as if the ship got hit
                   self._ship_hit()
                   break
              

    def check_alien_boss_bottom(self):
          """Check if alien boss have reached the bottom of the screen."""
          if self.alienboss.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                
              
 
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()
        for bullet in self.bulletboss.sprites():
              bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)


        # Draw the score information
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
             self.play_button.draw_button()
             self.hard_button.draw_button()
             self.medium_button.draw_button()
     
        
        if self.alienboss:        
          self.alienboss.blitme()


        # Make the most recently drawn screen visible.
        pygame.display.flip()
        



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai =  AlienInvasion()
    ai.run_game()









    



