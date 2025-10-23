import pygame
import sys
from settings import Settings
from character import Character

class GameCharacter:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Game Character")

        self.gap = Character(self)

    def run_game(self):
        while True:
             self._check_events()
             self._update_screen()
             self.clock.tick(60)
             
            
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.gap.blitme()
     
            pygame.display.flip()
            
            

if __name__ == '__main__':
    gc = GameCharacter()
    gc.run_game()