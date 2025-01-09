import pygame, sys
from math import sqrt
from random import randint
pygame.init()
screen = pygame.display.set_mode((825, 550))
pygame.display.set_caption("Space Invaders For Mac")
pygame.display.set_icon(pygame.image.load("black.jpg"))
background = pygame.image.load("background.jpg")
player = pygame.image.load("spaceship.png")
alien = pygame.image.load("alien.png")
laser = pygame.image.load("laser.png")
def alien_location():
    kobe = randint(0, 800)
    print(kobe, type(kobe))
    return kobe
playerX = 375
playerX_move = 0
bulletY_move = 0
bulletY = 490
alienX = alien_location()
alienY = 0
alienX_move = 5
fired = False




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_move = 5
            elif event.key == pygame.K_LEFT:
                playerX_move = -5
            elif event.key == pygame.K_UP:
                bulletY_move = -25
                fired = True
                
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    playerX_move = 0 
    if alienX < 7:
        alienY += 20
        alienX_move = 5
    elif alienX > 770:
        alienY += 20
        alienX_move = -5

        
    alienX += alienX_move
    playerX += playerX_move
    bulletY += bulletY_move
    if bulletY < 0:
        bulletY = 490
        bulletY_move = 0
        fired = False
    if playerX > 756:
        playerX_move = 0
    elif playerX < 0:
        playerX_move = 0
    screen.blit(background, (0, 0))
    if fired == False:
        bulletX = playerX + 15
        screen.blit(laser, (playerX + 18, bulletY))
    elif fired == True:
        screen.blit(laser, (bulletX, bulletY))
    screen.blit(player, (playerX, 480))
    screen.blit(alien, (alienX, alienY))
    distance = sqrt(pow((alienX - bulletX), 2) + pow((alienY - bulletY), 2))
    edistance = sqrt(pow((alienX - playerX), 2) + pow((alienY - 480), 2))
    if distance < 27:
        alienX = alien_location()
        alienY = 0
    if edistance < 50:
        print("nanayı yemedin mi")
    pygame.display.update()
    pygame.time.Clock().tick(60)