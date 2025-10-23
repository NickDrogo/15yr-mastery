import pygame 

import sys
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Key Press Example")

WHITE = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.key} ({pygame.key.name(event.key)})")
        elif event.type == pygame.KEYUP:
            print(f"Key released: {event.key} ({pygame.key.name(event.key)})")



    screen.fill(WHITE)
    pygame.display.flip()