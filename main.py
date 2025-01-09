import pygame, sys
from math import sqrt
from random import randint
pygame.init()
screen = pygame.display.set_mode((825, 550))
pygame.display.set_caption("Space Invaders For Mac")
pygame.display.set_icon(pygame.image.load("icon.png"))
background = pygame.image.load("background.jpg")
player = pygame.image.load("spaceship.png")
alien = pygame.image.load("alien.png")
alien2 = pygame.image.load("alien.png")
laser = pygame.image.load("laser.png")
laser_sound = pygame.mixer.Sound("laser.mp3")
death_sound = pygame.mixer.Sound("death.mp3")
bg_music = pygame.mixer_music.load("bg_music.mp3")
font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 50)
score = 0
txt = False
def death_text():
    if txt == True:
        death_txt = font2.render("GAME OVER ", True, (255, 255, 255))
        screen.blit(death_txt, (250, 200))
def score_func():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (5, 5))
playerX = 375
playerX_move = 0
bulletY_move = 0
bulletY = 490
alienX = randint(0, 800)
alienX2 = randint(0, 800)
alienY = 0
alienY2 = 0
alienX_move = 5
alienX2_move = 5
fired = False
alien_list = []
alien_x = []
alien_y = []
alien_move = []
number_enemies = range(10)
for num in number_enemies:
    alien_list.append(alien)
    alien_x.append(randint(0,800))
    alien_y.append(randint(0,60))
    alien_move.append(5)

pygame.mixer_music.play(-1)
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
    
    if bulletY < 0:
        bulletY = 490
        bulletY_move = 0
        fired = False
    if playerX > 756:
        playerX_move = 0
        if event.key == pygame.K_LEFT:
                playerX_move = -5
    elif playerX < 0:
        playerX_move = 0
        if event.key == pygame.K_RIGHT:
            playerX_move = 5

    screen.blit(background, (0, 0))
    if fired == False:
        bulletX = playerX + 15
        screen.blit(laser, (playerX + 18, bulletY))
    elif fired == True:
        screen.blit(laser, (bulletX, bulletY))
    screen.blit(player, (playerX, 480))
    distance = sqrt(pow((alienX - bulletX), 2) + pow((alienY - bulletY), 2))
    edistance = sqrt(pow((alienX - playerX), 2) + pow((alienY - 480), 2))

    for num in number_enemies:
        screen.blit(alien_list[num], (alien_x[num], alien_y[num]))
        distance = sqrt(pow((alien_x[num] - bulletX), 2) + pow((alien_y[num] - bulletY), 2))
        edistance = sqrt(pow((alien_x[num] - playerX), 2) + pow((alien_y[num] - 480), 2))
        if alien_x[num] < 7:
            alien_y[num] += 50
            alien_move[num] = 5
        elif alien_x[num] > 770:
            alien_y[num] += 50
            alien_move[num] = -5
        alien_x[num] += alien_move[num]
        
        if distance < 27:
            alien_x[num] = randint(0, 800)
            alien_y[num] = 0
            score += 1
            bulletY = 490
            bulletY_move = 0
            fired = False
            pygame.mixer.Sound.play(laser_sound)
        if edistance < 50:
            pygame.mixer_music.stop()
            pygame.mixer.Sound.play(death_sound)
            for num in number_enemies:
                alien_y[num] = 2000
            txt = True
            






    playerX += playerX_move
    bulletY += bulletY_move
    score_func()
    death_text()
 
    

    pygame.display.update()
    pygame.time.Clock().tick(60)