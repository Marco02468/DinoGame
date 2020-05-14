import math
import pygame

pygame.init()

screen = pygame.display.set_mode((200, 150))
gameIcon = pygame.image.load('dino.png')
pygame.display.set_icon(gameIcon)

gridImg = pygame.image.load('gitter.png')

floorImg = pygame.image.load('floor.png')
floor_x = 0
floor_y = 130
floor_x_change = -10

white = [140, 140, 140]
red = [255, 0, 0]

pygame.display.set_caption('Demo')

playerImg = pygame.image.load('player.png')
playerImg2 = pygame.image.load('player_down.png')
player_x = 20
player_y = 90
player_y_change = 0
jumping_state = "ready"
crouching_state = "ready"

enemyImg = pygame.image.load('enemy.png')
enemy_x = 200
enemy_y = 90
enemy_x_change = -10

enemyImg2 = pygame.image.load('enemy2.png')
enemy_x2 = enemy_x + 100
enemy_y2 = 100
enemy_x_change2 = -10


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def enemy2(x, y):
    screen.blit(enemyImg2, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def floor(x, y):
    screen.blit(floorImg, (x, y))


def grid(x, y):
    screen.blit(gridImg, (x, y))


def collision(player_x, player_y, enemy_x, enemy_y):
    distance = math.sqrt((math.pow(player_x - enemy_x, 2)) + (math.pow(player_y - enemy_y, 2)))
    if distance == 10:
        print("collision")
        return True
    else:
        return False


def collision2(player_x, player_y, enemy_x, enemy_y):
    distance = math.sqrt((math.pow(player_x - enemy_x, 2)) + (math.pow(player_y - enemy_y, 2)))
    if distance == 10:
        print("collision")
        return True
    else:
        return False


font = pygame.font.Font('freesansbold.ttf', 30)


def text_game_over():
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (0, 0))


timer = 0
timer2 = 0
running = True

while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    timer += 1

    if timer >= 160:

        timer = 0

        if floor_x >= -180:
            floor_x += floor_x_change
        else:
            floor_x = 0

        enemy_x += enemy_x_change
        enemy_x2 += enemy_x_change2

    if enemy_x < 0:
        enemy_x = 200

    if enemy_x2 < 0:
        enemy_x2 = enemy_x + 100

    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and player_y == 90:
            print("unten Taste")
            playerImg = pygame.image.load('player_down.png')
            player_y = 120
            jumping_state = "jump"
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            print("released")
            playerImg = pygame.image.load('player.png')
            player_y = 90
            jumping_state = "ready"

    if keys[pygame.K_SPACE] and jumping_state == "ready":
        jumping_state = "jump"
        print("Space pressed")
        player_y_change = 10

    timer2 += 1

    if timer2 >= 90:
        timer2 = 0

        player_y -= player_y_change

        if player_y <= 0:
            player_y_change = -10
            player_y -= player_y_change

        if player_y == 90:
            jumping_state = "ready"
            player_y_change = 0

    game_over = collision(player_x, player_y, enemy_x, enemy_y)
    game_over2 = collision2(player_x, player_y, enemy_x2, enemy_y2)

    if game_over or game_over2:
        # enemy_x = 10
        # player_x = -100
        # screen.fill(red)
        break

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    enemy2(enemy_x2, enemy_y2)
    floor(floor_x, floor_y)
    grid(0, 0)

    pygame.display.update()
