import sys
from ship import Ship
from settings import Settings
from bullet import Bullets
from target  import Target
from time import sleep
from buttons import Buttons


import pygame

class TargetPractise:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # , pygame.FULLSCREEN)
        pygame.display.set_caption("Target Practise")

        
        self.game_active = False

        # Make the play button.
        self.play_button = Buttons(self, "Play")


        
        self.misses = 0
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
   

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events() 
            if self.game_active:
               self.ship.update()
               self._update_bullets()
               self.target.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
         if button_clicked and not self.game_active:
              # Reset the game statistics
              self.settings.initialize_dynamic_settings()
              self._start_game()
     

         
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()
        elif event.key == pygame.K_p:
             self._start_game()
             

    def _check_keyup_events(self, event):
         """Respond to key releases"""    
         if event.key == pygame.K_UP:
                self.ship.moving_up = False
         elif event.key == pygame.K_DOWN:   
                self.ship.moving_down = False

    def _fire_bullet(self):
         """Create a new bullet and add it to the bullets group."""
         if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)


    
    def _update_bullets(self):
         """Update position of bullets and get rid of old bullets."""
         # Update bullet positons
         # Get rid of bullets that have disappeared;
         self.bullets.update()
    
         for bullet in self.bullets.copy():
              if bullet.rect.left >= self.settings.screen_width :
                    self.bullets.remove(bullet)
                    self.misses += 1
                    if self.misses >= 3:
                         sleep(2.0)
                         self._start_game()

         self._check_bullet_target_collisions()
              

         
    def _check_bullet_target_collisions(self):
         """Respond to bullet-alien collisions."""
         # Remove any bullets that have collided.
         collisions = pygame.sprite.spritecollide(self.target, self.bullets, True)
         if collisions:
                   sleep(2.0)
                   self.settings.increase_speed()
                   self._start_game()

                   
    
    def _start_game(self):
         self.bullets.empty()
         self.misses = 0
         self.game_active = True
         self.ship.center_ship()


          # Hide  the mouse cursor
         pygame.mouse.set_visible(False)



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()
        self.ship.blitme()
        self.target.blitme()
     

        # Draw the play button if the game is inactive.
        if not self.game_active:
             self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        



if __name__ == '__main__':
    # Make a game instance, and run the game.
    tp =  TargetPractise()
    tp.run_game()









    



