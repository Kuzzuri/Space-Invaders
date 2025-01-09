import pygame, sys
pygame.init()
screen = pygame.display.set_mode((850, 500))
pygame.display.set_caption("Space Invaders For Mac")
pygame.display.set_icon(pygame.image.load("black.jpg"))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()