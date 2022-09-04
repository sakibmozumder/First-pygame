import random
import math
import os
import pygame

# initialize pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
menuScreen = pygame.display.set_mode((800, 600))
# Title and icon
pygame.display.set_caption("My First Game v 2.0")
icon = pygame.image.load("AceOfSpades.png")
pygame.display.set_icon(icon)


# Create elements of the game
class Characters:
    def __init__(self, chrImage, x, y, scaleX, scaleY):
        self.image = pygame.image.load(chrImage)
        self.x = x
        self.y = y
        self.scaleX = scaleX
        self.scaleY = scaleY

    def scale(self):
        return pygame.transform.scale(self.image, (self.scaleX, self.scaleY))


# Create collision rule
def collision(x1, x2, y1, y2, condition):
    distance = math.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)))
    return distance <= condition

def collisionGO(x1, x2, y1, y2):
    return x1 - img_grenade.get_width() + 10 <= x2 <= x1 + skH.get_width() - 20 and \
           y1 - img_grenade.get_height() + 20 <= y2 <= y1 + skH.get_height()


if __name__ == "__main__":
    # Set up the game elements
    road = Characters("road.png", 0, 0, 800, 800)
    imgRoad = road.scale()
    road2 = Characters("road.png", 0, -720, 800, 800)
    imgRoad2 = road.scale()
    sh = Characters("saitama.png", 400, 480, 60, 80)
    skH = sh.scale()
    grenade = Characters("grenade.png", random.randint(160, 580), 120, 30, 40)
    img_grenade = grenade.scale()
    missile = Characters("missile.png", sh.x + 15, sh.y - 40, 30, 40)
    img_missile = missile.scale()
    horizontalMove = 0
    verticalMove, missileMove = 0, 0
    missile_launch = False
    grenade_launch = False
    point = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    fontScore = pygame.font.Font('freesansbold.ttf', 20)
    textx = 10
    texty = 10
    fontGO = pygame.font.Font('freesansbold.ttf', 32)
    textGOx = -300
    textGOy = 250
    gameCont = True
    playFont = pygame.font.Font('freesansbold.ttf', 17)
    playX = 357
    playY = 165
    # Game loop
    menu = True
    running = True
    new_game = True
    go_back = False
    reset = False
    highScore = "00"
    if os.path.exists("highScore.log"):
        f = open("highScore.log", "r")
        highScore = f.read()
        f.close()
    else:
        f = open("highScore.log", "w")
        f.write(highScore)
        f.close()

    while running:
        while menu:
            menuScreen.fill((255, 255, 255))
            pygame.draw.rect(menuScreen, (100, 0, 100), (350, 150, 100, 50), border_radius=10)
            screen.blit(playFont.render("New Game", True, (255, 255, 255)), (playX, playY))
            pygame.draw.rect(menuScreen, (100, 0, 100), (350, 225, 100, 50), border_radius=10)
            screen.blit(playFont.render("Exit", True, (255, 255, 255)), (playX + 25, playY + 75))
            screen.blit(playFont.render("High Score:", True, (0, 0, 0)), (playX - 5, playY + 150))
            screen.blit(playFont.render(str(highScore), True, (0, 0, 0)), (playX + 25, playY + 180))
            mouse = pygame.mouse.get_pos()
            if 350 <= mouse[0] <= 450 and 150 <= mouse[1] <= 200:
                screen.blit(playFont.render("New Game", True, (50, 205, 50)), (playX, playY))
            if 350 <= mouse[0] <= 450 and 225 <= mouse[1] <= 275:
                screen.blit(playFont.render("Exit", True, (50, 205, 50)), (playX + 25, playY + 75))
            for event in pygame.event.get():
                # pygame.QUIT is for the Close button
                if event.type == pygame.QUIT:
                    menu = False
                    running = False
                    new_game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 350 <= mouse[0] <= 450 and 150 <= mouse[1] <= 200:
                        menu = False
                        new_game = True
                        gameCont = True
                    if 350 <= mouse[0] <= 450 and 225 <= mouse[1] <= 275:
                        menu = False
                        new_game = False
                        running = False
            pygame.display.update()
        # Change Background
        if new_game:
            screen.fill((255, 255, 255))
            screen.blit(imgRoad, (road.x, road.y))
            screen.blit(imgRoad2, (road2.x, road2.y))
            for event in pygame.event.get():
                # pygame.QUIT is for the Close button
                if event.type == pygame.QUIT:
                    new_game = False
                    running = False
                # check whether a keystroke is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 800 and 0 <= mouse[1] <= 600 and go_back:
                        menu = True
                        new_game = True
                        gameCont = True
                        reset = True
                if event.type == pygame.MOUSEBUTTONUP:
                    go_back = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and gameCont:
                        if sh.x <= 550:
                            horizontalMove = 3
                    if event.key == pygame.K_LEFT and gameCont:
                        if sh.x >= 160:
                            horizontalMove = -3
                    if event.key == pygame.K_UP and gameCont:
                        verticalMove = -3
                    if event.key == pygame.K_DOWN and gameCont:
                        verticalMove = 3
                    if event.key == pygame.K_SPACE and gameCont:
                        missile_launch = True
                        missileMove = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        horizontalMove = 0
                    if event.key == pygame.K_LEFT:
                        horizontalMove = 0
                    if event.key == pygame.K_UP:
                        verticalMove = 0
                    if event.key == pygame.K_DOWN:
                        verticalMove = 0

            # call the elements
            screen.blit(skH, (sh.x, sh.y))
            screen.blit(img_missile, (missile.x, missile.y))
            screen.blit(img_grenade, (grenade.x, grenade.y))

            if gameCont:
                grenade.y += 2
                road.y += 1
                road2.y += 1
            if grenade.y > 600 and gameCont:
                grenade.y = -80
                grenade.x = random.randint(160, 580)
            if road.y > 719 and gameCont:
                road.y = -719
            if road2.y > 719 and gameCont:
                road2.y = -719

            sh.x += horizontalMove
            if sh.x > 550 or sh.x < 160:
                horizontalMove = 0
            # sh.y += verticalMove
            if sh.y >= 520 or sh.y <= 0:
                verticalMove = 0
            if missile_launch:
                missile.x += 0
                missile.y += missileMove
            else:
                missile.x = sh.x + 15
            if missile.y < -40:
                missile_launch = False
                missile.y = sh.y - 40
                missile.x = sh.x + 15

            if collision(missile.x, grenade.x, missile.y, grenade.y, 10):
                grenade.y = 700
                missile.y = -80
                point += 5

            if collisionGO(sh.x, grenade.x, sh.y, grenade.y):
                horizontalMove, verticalMove, missileMove = 0, 0, 0
                gameCont = False
                screen.blit(font.render("Game Over", True, (255, 0, 0)), (textGOx + 600, textGOy))
                screen.blit(font.render("He is bald now", True, (255, 0, 255)), (textGOx + 580, textGOy + 50))
                screen.blit(font.render("Your Score: " + str(point), True, (0, 255, 0)), (textGOx + 580, textGOy + 100))
                screen.blit(font.render("Click Anywhere", True, (0, 0, 255)), (textGOx + 570, textGOy + 150))
                go_back = True
                if point > int(highScore):
                    highScore = str(point)
                    f = open("highScore.log", "w")
                    f.write(highScore)
                    f.close()
                # pygame.display.update()
                # menu = True
            screen.blit(fontScore.render("Score: " + str(point), True, (0, 0, 0)), (textx, texty))
            # You have to update everytime you change
            # something in the display
            pygame.display.update()
            if reset:
                sh.x = 400
                sh.y = 480
                missile.x, missile.y = sh.x, sh.y
                grenade.x = random.randint(160, 580)
                grenade.y = 120
                road.x, road.y = 0, -100
                textGOx = -300
                textGOy = 250
                point = 0
                reset = False
                missile_launch = False
