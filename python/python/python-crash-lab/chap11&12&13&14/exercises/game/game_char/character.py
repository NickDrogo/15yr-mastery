import pygame

class Character:
    def __init__(self, gc_game):

        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('chap11&12/game/images/character.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


        