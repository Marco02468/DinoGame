from Renderer import Renderer
import pygame

pygame.init()
pygame.display.set_mode((100, 100))
pygame.joystick.init()

running = True

while running:

    jumpingstate = "ready"

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            
    event = pygame.event.poll()

    # Keyboard
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and jumpingstate == "ready":
            Renderer.jump()

        if event.key == pygame.K_DOWN:
            jumpingstate = "not_ready"
            Renderer.generateDuckedDino()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            jumpingstate = "ready"
            Renderer.generateDino()

    # NES Controller
    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 1 and jumpingstate == "ready":  # A Button
            Renderer.jump()

        if event.button == 0:  # B Button
            jumpingstate = "not_ready"
            Renderer.generateDuckedDino()

    if event.type == pygame.JOYBUTTONUP:
        if event.button == 0:
            Renderer.generateDino()
            jumpingstate = "ready"
