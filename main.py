import pygame
import sys
from pygame import *

pygame.init()

def Score_MAIN():
    score_name = open('score_name', 'r')
    score_points = open('score_points', 'r')
    VSN, VSP = [], []
    VSN = score_name.readlines()
    VSP = score_points.readlines()
    player_score = []
    for i in range(len(VSP)):
        dic_append = [VSN[i], VSP[i]]
        player_score.append(dic_append)
    for i in range(len(VSP)):
        for o in range(len(VSN)):
            element = player_score[i]
            if player_score[i][1] <= player_score[o][1]:
                player_score[i] = player_score[o]
                player_score[o] = element
    player_score  = player_score[::-1]
    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                running = False
        text('Player:', font, (255, 255, 255), screen, 40, 0, (110, 40))
        text('Score:', font, (255, 255, 255), screen, 180, 0, (110, 40))
        text("Press any key to go back", font, (255, 255, 255), screen, 450, 870, [450, 30])
        for i in range(len(player_score)):
            text(player_score[i][0], font_score, (255, 255, 255), screen, 40, (i*50)+70, (60, 40))
            text(player_score[i][1], font_score, (255, 255, 255), screen, 180, (i*50)+70, (60, 40))

        pygame.display.update()
        pygame.time.delay(60)
    score_name.close()
    score_points.close()


def Score_SAVE(score_point):
    pygame.time.delay(600)
    score_name = open('score_name', 'a')
    score_points = open('score_points', 'a')
    name = str('')
    score_point = str(score_point)
    while len(name) < 3:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                letra = pygame.key.name(event.key)
                letra = letra.upper()
                letra = letra[0]
                name += letra
        text("Player", font_score, (255, 255, 255), screen, 0, 390, [110, 40])
        text("Score", font, (255, 255, 255), screen, 140, 390, (110, 40))
        text(score_point, font_score, (255, 255, 255), screen, 410, 460, [60, 40])
        for i in range(len(name)):
            text(name[i], font_score, (255, 255, 255), screen, i*60, 460, [60, 40])

        pygame.display.update()
        pygame.time.delay(60)
    score_name.write(name+'\n')
    score_points.write(score_point+'\n')
    score_name.close()
    score_points.close()

def Lives(lives):
    livesX = [780, 810, 840]
    for i in range(len(lives)):
        screen.blit(lives[i], [livesX[i], 0])


def Round(round, pos):
    time = 0
    while time < 30:
        round = str(round)
        screen.blit(background, (0, 0))
        screen.blit(playerImg, (pos[0], pos[1]))
        text('Round  ' + round, font, (255, 255, 255), screen, 300, 400, [300, 80])
        pygame.display.update()
        time += 1
        pygame.time.delay(60)


def restart(al, ay, ax):
    al, ay, ax = [], [], []
    for i in range(10):
        for o in range(10):
            al.append(alien)
            ay.append((o * 35) + 50)
        ax.append((i * 40) + 400)
    return al, ay, ax


def game_over():
    time = 0
    while time < 30:
        screen.blit(background, (0, 0))
        text("Game Over", font, (255, 255, 255), screen, 300, 400, [300, 80])
        time += 1
        pygame.display.update()
        pygame.time.delay(60)


def death(livesNum):
    time = 0
    if len(livesNum) > 1:
        livesNum = str(len(livesNum))
        while time < 30:
            screen.blit(background, (0, 0))
            screen.blit(playerImg, (pos[0], pos[1]))
            text(livesNum + " lives left", font, (255, 255, 255), screen, 150, 400, [600, 80])
            pygame.display.update()
            time += 1
            pygame.time.delay(60)
    elif len(livesNum) == 1:
        while time < 30:
            screen.blit(background, (0, 0))
            screen.blit(playerImg, (pos[0], pos[1]))
            text("Last life", font, (255, 255, 255), screen, 150, 400, [600, 80])
            pygame.display.update()
            time += 1
            pygame.time.delay(60)


def text(text, font, color, surface, x, y, size):
    texto = font.render(text, 1, color)
    textorect = texto.get_rect()
    textorect.topleft = (x, y)
    texto = pygame.transform.scale(texto, size)
    surface.blit(texto, textorect)


def game(pos, PX_change, B_check, BX, BY, AL, AX, AY):
    score_point = 0
    lives_icon = playerImg
    lives_icon = pygame.transform.scale(lives_icon, [30, 30])
    lives = [lives_icon, lives_icon, lives_icon]
    round = 0
    Round(round, pos)
    AX_change = 8
    AY_change = 0
    while True:
        # RGB
        screen.fill(color)
        # Background
        screen.blit(background, (0, 0))
        # Score and lives
        SP = str(score_point)
        text('Score: ', font, (255, 255, 255), screen, 10, 0, [120, 30])
        text(SP, font_score, (255, 255, 255), screen, 140, 0, [30, 30])
        text('Lives: ', font, (255, 255, 255), screen, 660, 0, [120, 30])
        Lives(lives)
        # Exit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Movement of the ship
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    PX_change = 10
                elif event.key == pygame.K_LEFT:
                    PX_change = -10
                if event.key == pygame.K_SPACE:
                    if B_check == "ready":
                        B_check = "moving"
                        BX = pos[0]+20
                        BY = pos[1]
                        pygame.mixer.music.load("sounds/pew.mp3")
                        pygame.mixer_music.play(0, 0)
            if event.type == pygame.KEYUP:
                PX_change = 0

        # Blit alien
        x = -1
        for i in range(len(AL)):
            if i % 10 == 0:
                x += 1
            screen.blit(AL[i], [AX[x], AY[i]])

        # Movement of the alien

        for i in range(100):
            if AX[i//10] <= 0 and AL[i] != transparent:
                AX[i//10] = 0
                AX_change = -AX_change
                AY = [y + AY_change for y in AY]
                AY_change += 2
                break
            if AX[(100-i-1)//10] >= (width - 70) and AL[i] != transparent:
                AX[(100-i-1)//10] = (width - 70)
                AX_change = -AX_change
                AY = [y + AY_change for y in AY]
                AY_change += 2
                break
        AX = [x + AX_change for x in AX]

        # Movement of the bullet
        if B_check == "moving":
            BY -= 40
            screen.blit(bullet, [BX, BY])
            if BY <= 0:
                B_check = "ready"
            y = 0
            for i in range(len(AX)):
                for o in range(10):
                    if AY[o] <= BY <= AY[o] + 35 and AX[i] <= BX <= AX[i] + 35 and AL[y] != transparent:
                        score_point += 100
                        AL[y] = transparent
                        B_check = "ready"
                    y += 1

        pos[0] += PX_change
        if pos[0] <= 0:
            pos[0] = 0
        if pos[0] >= (width - 60):
            pos[0] = (width - 60)

        #Restart
        AL_count = AL.count(transparent)
        if AL_count == 100:
            AL, AY, AX = restart(AL, AY, AX)
            round += 1
            Round(round, pos)

        # Game over
        for i in range(100):
            if AY[i] >= height - 70 and AL[i] != transparent:
                if len(lives) - 1 > 0:
                    lives.pop(0)
                    death(lives)
                    AL, AY, AX = restart(AL, AY, AX)
                else:
                    game_over()
                    Score_SAVE(score_point)
                    return 0

        #Update
        screen.blit(playerImg, pos)
        pygame.display.update()
        pygame.time.delay(10)


# Create the screen
size = width, height = 900, 900
screen = pygame.display.set_mode(size)
color = 255, 255, 255
transparent = pygame.image.load("images/transparent.png")
background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(background, [900, 900])

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# Font
font_score = pygame.font.SysFont(None, 50)
font = pygame.font.Font("font/ZealotCollegeItalic-Y24O.ttf", 50)
startX, startY = 40, 40

# Player
pos = [420, 830]
playerImg = pygame.image.load("images/nave.png")
playerImg = pygame.transform.scale(playerImg, (60, 60))
playerX_change = 0

# Enemy
alien = pygame.image.load("images/alien.png")
alien = pygame.transform.scale(alien, (35, 35))
alienL, alienY, alienX = [], [], []

for i in range(10):
    for o in range(10):
        alienL.append(alien)
        alienY.append((o * 35) + 50)
    alienX.append((i * 40) + 400)

# Bullets
bullet = pygame.image.load("images/bala.png")
bullet = pygame.transform.scale(bullet, [20, 15])
bulletX, bulletY, bulletCheck = pos[0], pos[1], "ready"


def main_menu():
    pygame.mixer.music.load("sounds/background_main.mp3")
    pygame.mixer.music.play(0, 0)
    while True:
        click = False
        screen.blit(background, (0, 0))
        text('Space Invaders', font, (255, 255, 255), screen, 175, 150, [550, 80])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        button_start = pygame.Rect(350, 400, 200, 60)
        button_score = pygame.Rect(350, 500, 200, 60)

        if button_start.collidepoint(mx, my):
            if click:
                pygame.mixer.music.stop()
                game(pos, playerX_change, bulletCheck, bulletX, bulletY, alienL, alienX, alienY)
        if button_score.collidepoint(mx, my):
            if click:
               Score_MAIN()

        pygame.draw.rect(screen, (255, 255, 255), button_start)
        text('Start', font, (255, 0, 0), screen, 370, 395, [160, 70])
        pygame.draw.rect(screen, (255, 255, 255), button_score)
        text('Score', font, (255, 0, 0), screen, 370, 495, [160, 70])

        pygame.display.update()
        pygame.time.delay(100)


main_menu()