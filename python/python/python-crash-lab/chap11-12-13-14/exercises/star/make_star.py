import pygame
from pygame.sprite  import Sprite

class MakeStar(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        
        self.screen = ai_game.screen
        
        self.image = pygame.image.load("chap11&12&13&14/star/images/stake.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


