from Game import Game
import pygame

pygame.init()
pygame.display.set_mode((100, 100))
pygame.joystick.init()

running = False
x = Game()
event = pygame.event.poll()

    # Keyboard
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE: #and jumpingstate == "ready":
        print("space")
while running:

    jumpingstate = "ready"

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

    event = pygame.event.poll()

    # Keyboard
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and jumpingstate == "ready":
            print("space")
            x.jump()

        if event.key == pygame.K_DOWN:
            print("down")
            jumpingstate = "not_ready"
            x.duck()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            print("up")
            jumpingstate = "ready"
            dino = x.generateDino()
            x.drawDino(dino)

    # NES Controller
    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 1 and jumpingstate == "ready":  # A Button
            x.jump()

        elif event.button == 0:  # B Button
            jumpingstate = "not_ready"
            x.generateDuckedDino()

    if event.type == pygame.JOYBUTTONUP:
        if event.button == 0:
            x.generateDino()
            jumpingstate = "ready"
