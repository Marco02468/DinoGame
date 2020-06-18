from TextRenderer import TextRenderer
from Grids import Grid
import pygame
from Ressource import Ressource


r = TextRenderer(15, 20)
g = Grid(r.width, r.height, r)
ressource = Ressource()

pygame.init()
pygame.display.set_mode((100, 100))
pygame.joystick.init()


g.render(ressource.startbild)
ressource.start()
ressource.color_game()


#dino_jump()
#render_play()
#g.render(ressource.play)

running = True

while running:
    running_game = False
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

    event = pygame.event.poll()

    # Keyboard
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            running = False
            print("Enter")
            for i in range(len(ressource.play)):
                ressource.play[i][2] = 7
            g.render(ressource.play)
            from Game import Game

            x = Game()

        if event.key == pygame.K_a:
            running = False
            print("Enter")
            for i in range(len(ressource.play)):
                ressource.play[i][2] = 7
            g.render(ressource.play)
            from Game_Ai import GameAi

            y = GameAi()
            y.start()

        if event.key == pygame.K_b:
            running = False

    # SNES
    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 1 or event.button == 0:  # A or B Button
            for i in range(len(ressource.play)):
                ressource.play[i][2] = 7
            from Game import Game

            x = Game()
            g.render(ressource.play)
            print("hey")
