import sys
from settings import Settings
from rain import Rain



import pygame

class ShowRain:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # , pygame.FULLSCREEN)
        pygame.display.set_caption("RAIN FAll")

        self.rain = pygame.sprite.Group()
        self._create_fleet()
        
    

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events() 
            self.update_rain()
            self._update_rain()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            
        
    def _create_fleet(self):
         
         rain = Rain(self)
         rain_width, rain_height = rain.rect.size

         current_x, current_y = rain_width, rain_height
         while current_y < (self.settings.screen_height - (3 * rain_height)):
            while current_x < (self.settings.screen_width - (2 * rain_width)):
                self._create_alien(current_x, current_y)
                current_x += 2 * rain_width

            # Finished a row; reset x value, and increment y value.
            current_x = rain_width
            current_y += 2 * rain_height

    def _create_alien(self, x_position, y_positon):
         """Create an rain and place it in the row."""
         new_rain = Rain(self)
         new_rain.x = x_position
         new_rain.rect.x = x_position
         new_rain.rect.y = y_positon
         self.rain.add(new_rain)

    def _check_fleet_edges(self):
         """Respond appropriately if any rains have reached an edge"""
         for rain in self.rain.sprites():
              if rain.check_edges():
                   self._change_fleet_direction()
                   break

    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleet's direction."""
         for rain in self.rain.sprites():
              rain.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1

    def update_rain(self):
         """Update the positions of all rains in the fleet."""
         self._check_fleet_edges()
         self.rain.update()
 
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rain.draw(self.screen)


        # Make the most recently drawn screen visible.
        pygame.display.flip()

    
    
    def _update_rain(self):
         self.rain.update()
         screen_rect = self.screen.get_rect()

         for raindrop in self.rain.copy():
             if raindrop.rect.top >= screen_rect.bottom:
                 self.rain.remove(raindrop)
         if not self.rain:
             self._create_fleet()
             

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sr =  ShowRain()
    sr.run_game()









    



