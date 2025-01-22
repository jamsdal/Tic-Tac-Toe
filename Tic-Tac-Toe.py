import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
click = False
clear = False
a1, b1, c1, a2, b2, c2, a3, b3, c3 = 0, 0, 0, 0, 0, 0, 0, 0, 0
player = 1
dt = 0

while running:
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.KEYUP:
            clear = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                clear = True

    screen.fill("black")

    pygame.draw.line(screen, "white", ((screen.get_width() / 3), 0),
                     ((screen.get_width() / 3), screen.get_height()), width=5)
    pygame.draw.line(screen, "white", (((screen.get_width() * 2) / 3), 0),
                     (((screen.get_width() * 2) / 3), screen.get_height()), width=5)
    pygame.draw.line(screen, "white", (0, (screen.get_height() / 3)),
                     (screen.get_width(), (screen.get_height() / 3)), width=5)
    pygame.draw.line(screen, "white", (0, ((screen.get_height() * 2) / 3)),
                     (screen.get_width(), ((screen.get_height() * 2) / 3)), width=5)

    if click:
        pygame.event.wait(pygame.MOUSEBUTTONUP)
        mouse = pygame.mouse.get_pos()
        if (mouse[0] < (screen.get_width() / 3)) and (mouse[1] < (screen.get_height() / 3)):
            if a1 == 0:
                a1 = player
        elif ((mouse[0] < ((screen.get_width() * 2) / 3)) and (mouse[0] > ((screen.get_width()) / 3))) and (mouse[1] < (screen.get_height() / 3)):
            if b1 == 0:
                b1 = player
        elif (mouse[0] > ((screen.get_width() * 2) / 3)) and (mouse[1] < (screen.get_height() / 3)):
            if c1 == 0:
                c1 = player
        elif (mouse[0] < (screen.get_width() / 3)) and ((mouse[1] > (screen.get_height() / 3)) and (mouse[1] < ((screen.get_height() * 2) / 3))):
            if a2 == 0:
                a2 = player
        elif ((mouse[0] < ((screen.get_width() * 2) / 3)) and (mouse[0] > ((screen.get_width()) / 3))) and ((mouse[1] > (screen.get_height() / 3)) and (mouse[1] < ((screen.get_height() * 2) / 3))):
            if b2 == 0:
                b2 = player
        elif (mouse[0] > (screen.get_width() / 3)) and ((mouse[1] > (screen.get_height() / 3)) and (mouse[1] < ((screen.get_height() * 2) / 3))):
            if c2 == 0:
                c2 = player
        elif (mouse[0] < (screen.get_width() / 3)) and (mouse[1] > ((screen.get_height() * 2) / 3)):
            if a3 == 0:
                a3 = player
        elif ((mouse[0] < ((screen.get_width() * 2) / 3)) and (mouse[0] > ((screen.get_width()) / 3))) and (mouse[1] > ((screen.get_height() * 2) / 3)):
            if b3 == 0:
                b3 = player
        else:
            if c3 == 0:
                c3 = player

        click = False
        clear = False
        if player == 1:
            player = 2
        else:
            player = 1

    if a1 == 1:
        pygame.draw.line(screen, "red", (0, 0), ((screen.get_width() / 3), (screen.get_height() / 3)), width=3)
        pygame.draw.line(screen, "red", ((screen.get_width() / 3), 0), (0, (screen.get_height() / 3)), width=3)

    if clear:
        a1, b1, c1, a2, b2, c2, a3, b3, c3 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        player = 1

    clear = False
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
