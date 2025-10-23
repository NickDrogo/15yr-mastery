import pygame
import sys
from make_star import MakeStar
from settings import Settings
import random

class Star:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Display Star")

        self.bg_color = (235, 235, 235)
        self.star = pygame.sprite.Group()
        self._create_fleet()
        

    def run_game(self):
        while True:
            self.screen.fill(self.bg_color)
            self._end_display()
            self.star.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def _end_display(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        star = MakeStar(self)
        star_width, star_height =  star.rect.size
      
        current_x, current_y = star_width, star_height
        
        while current_y < (self.settings.screen_height - (3 * star_height)):
            while current_x < (self.settings.screen_width - (2 * star_width)):
                 self._create_star(current_x, current_y)
                 current_x += 2 * star_width

            current_x = star_width
            current_y += 2 * star_height


    def _create_star(self, x_position, y_position):
        new_star = MakeStar(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        scale = random.randint(4, 6)
        if scale == 5:
            self.star.add(new_star)



if __name__ == "__main__":
    sr = Star()
    sr.run_game()