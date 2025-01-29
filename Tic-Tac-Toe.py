import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
click = False
clear = False
change_player = False
cells = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player = 1
winning_player = 0
win_check = 0
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
            if cells[0] == 0:
                cells[0] = player
                change_player = True
        elif ((mouse[0] < ((screen.get_width() * 2) / 3)) and (mouse[0] > ((screen.get_width()) / 3))) and (mouse[1] < (screen.get_height() / 3)):
            if cells[1] == 0:
                cells[1] = player
                change_player = True
        elif (mouse[0] > ((screen.get_width() * 2) / 3)) and (mouse[1] < (screen.get_height() / 3)):
            if cells[2] == 0:
                cells[2] = player
                change_player = True
        elif (mouse[0] < (screen.get_width() / 3)) and ((mouse[1] > (screen.get_height() / 3)) and (mouse[1] < ((screen.get_height() * 2) / 3))):
            if cells[3] == 0:
                cells[3] = player
                change_player = True
        elif ((mouse[0] < ((screen.get_width() * 2) / 3)) and (mouse[0] > ((screen.get_width()) / 3))) and ((mouse[1] > (screen.get_height() / 3)) and (mouse[1] < ((screen.get_height() * 2) / 3))):
            if cells[4] == 0:
                cells[4] = player
                change_player = True
        elif (mouse[0] > (screen.get_width() / 3)) and ((mouse[1] > (screen.get_height() / 3)) and (mouse[1] < ((screen.get_height() * 2) / 3))):
            if cells[5] == 0:
                cells[5] = player
                change_player = True
        elif (mouse[0] < (screen.get_width() / 3)) and (mouse[1] > ((screen.get_height() * 2) / 3)):
            if cells[6] == 0:
                cells[6] = player
                change_player = True
        elif ((mouse[0] < ((screen.get_width() * 2) / 3)) and (mouse[0] > ((screen.get_width()) / 3))) and (mouse[1] > ((screen.get_height() * 2) / 3)):
            if cells[7] == 0:
                cells[7] = player
                change_player = True
        else:
            if cells[8] == 0:
                cells[8] = player
                change_player = True

        click = False
        clear = False
        if change_player:
            if player == 1:
                player = 2
            else:
                player = 1
        change_player = False

    if cells[0] == 1:
        pygame.draw.line(screen, "red", (10, 10), (((screen.get_width() / 3) - 10), ((screen.get_height() / 3) - 10)), width=5)
        pygame.draw.line(screen, "red", (((screen.get_width() / 3) - 10), 10), (10, ((screen.get_height() / 3) - 10)), width=5)
    elif cells[0] == 2:
        pygame.draw.circle(screen, "blue", ((screen.get_width() / 6), (screen.get_height() / 6)), (screen.get_height() / 7), width=5)
    if cells[1] == 1:
        (pygame.draw.line(screen, "red", (((screen.get_width() / 3) + 10), 10), ((((screen.get_width() * 2) / 3) - 10), ((screen.get_height() / 3) - 10)), width=5))
        pygame.draw.line(screen, "red", ((((screen.get_width() * 2) / 3) - 10), 10), (((screen.get_width() / 3) + 10), ((screen.get_height() / 3) - 10)), width=5)
    elif cells[1] == 2:
        pygame.draw.circle(screen, "blue", ((screen.get_width() / 2), (screen.get_height() / 6)), (screen.get_height() / 7), width=5)
    if cells[2] == 1:
        pygame.draw.line(screen, "red", ((((screen.get_width() * 2) / 3) + 10), 10), ((screen.get_width() - 10), ((screen.get_height() / 3) - 10)), width=5)
        pygame.draw.line(screen, "red", ((screen.get_width() - 10), 10), (((screen.get_width() / 3 * 2) + 10), ((screen.get_height() / 3) - 10)), width=5)
    elif cells[2] == 2:
        pygame.draw.circle(screen, "blue", (((screen.get_width() * 5) / 6), (screen.get_height() / 6)), (screen.get_height() / 7), width=5)
    if cells[3] == 1:
        pygame.draw.line(screen, "red", (10, ((screen.get_height() / 3) + 10)), (((screen.get_width() / 3) - 10), (((screen.get_height() * 2) / 3) - 10)),
                         width=5)
        pygame.draw.line(screen, "red", (((screen.get_width() / 3) - 10), ((screen.get_height() / 3) + 10)), (10, (((screen.get_height() * 2) / 3) - 10)),
                         width=5)
    elif cells[3] == 2:
        pygame.draw.circle(screen, "blue", ((screen.get_width() / 6), (screen.get_height() / 2)),
                           (screen.get_height() / 7), width=5)
    if cells[4] == 1:
        pygame.draw.line(screen, "red", (((screen.get_width() / 3) + 10), ((screen.get_height() / 3) + 10)),
                         ((((screen.get_width() * 2) / 3) - 10), (((screen.get_height() * 2) / 3) - 10)), width=5)
        pygame.draw.line(screen, "red", ((((screen.get_width() * 2) / 3) - 10), ((screen.get_height() / 3) + 10)),
                         (((screen.get_width() / 3) + 10), (((screen.get_height() * 2) / 3) - 10)), width=5)
    elif cells[4] == 2:
        pygame.draw.circle(screen, "blue", ((screen.get_width() / 2), (screen.get_height() / 2)),
                           (screen.get_height() / 7), width=5)
    if cells[5] == 1:
        pygame.draw.line(screen, "red", ((((screen.get_width() * 2) / 3) + 10), ((screen.get_height() / 3) + 10)),
                         ((screen.get_width() - 10), (((screen.get_height() * 2) / 3) - 10)), width=5)
        pygame.draw.line(screen, "red", ((screen.get_width() - 10), ((screen.get_height() / 3) + 10)),
                         (((screen.get_width() / 3 * 2) + 10), (((screen.get_height() * 2) / 3) - 10)), width=5)
    elif cells[5] == 2:
        pygame.draw.circle(screen, "blue", (((screen.get_width() * 5) / 6), (screen.get_height() / 2)),
                           (screen.get_height() / 7), width=5)
    if cells[6] == 1:
        pygame.draw.line(screen, "red", (10, (((screen.get_height() * 2) / 3) + 10)), (((screen.get_width() / 3) - 10), (screen.get_height() - 10)), width=5)
        pygame.draw.line(screen, "red", (((screen.get_width() / 3) - 10), (((screen.get_height() * 2) / 3) + 10)), (10, (screen.get_height() - 10)), width=5)
    elif cells[6] == 2:
        pygame.draw.circle(screen, "blue", ((screen.get_width() / 6), ((screen.get_height() * 5) / 6)), (screen.get_height() / 7), width=5)
    if cells[7] == 1:
        pygame.draw.line(screen, "red", (((screen.get_width() / 3) + 10), (((screen.get_height() * 2) / 3) + 10)), ((((screen.get_width() * 2) / 3) - 10), (screen.get_height() - 10)), width=5)
        pygame.draw.line(screen, "red", ((((screen.get_width() * 2) / 3) - 10), (((screen.get_height() * 2) / 3) + 10)), (((screen.get_width() / 3) + 10), (screen.get_height() - 10)), width=5)
    elif cells[7] == 2:
        pygame.draw.circle(screen, "blue", ((screen.get_width() / 2), ((screen.get_height() * 5)/ 6)), (screen.get_height() / 7), width=5)
    if cells[8] == 1:
        pygame.draw.line(screen, "red", ((((screen.get_width() * 2) / 3) + 10), (((screen.get_height() * 2) / 3) + 10)), ((screen.get_width() - 10), (screen.get_height() - 10)), width=5)
        pygame.draw.line(screen, "red", ((screen.get_width() - 10), (((screen.get_height() * 2) / 3) + 10)), (((screen.get_width() / 3 * 2) + 10), (screen.get_height() - 10)), width=5)
    elif cells[8] == 2:
        pygame.draw.circle(screen, "blue", (((screen.get_width() * 5) / 6), ((screen.get_height() * 5) / 6)), (screen.get_height() / 7), width=5)

    if clear:
        for cell in range(0,len(cells)):
            cells[cell] = 0
        player = 1

    win_check = 0
    for cell in cells:
        win_check += cell

    if win_check >= 7:
        if cells[0] == cells[1] and cells[1] == cells[2] and cells[0] != 0:
            winning_player = cells[0]
        elif cells[0] == cells[3] and cells[3] == cells[6] and cells[0] != 0:
            winning_player = cells[0]
        elif cells[0] == cells[4] and cells[4] == cells[8] and cells[0] != 0:
            winning_player = cells[0]
        elif cells[2] == cells[4] and cells[4] == cells[6] and cells[0] != 0:
            winning_player = cells[2]
        elif cells[1] == cells[4] and cells[4] == cells[7] and cells[0] != 0:
            winning_player = cells[1]
        elif cells[2] == cells[5] and cells[5] == cells[8] and cells[0] != 0:
            winning_player = cells[2]
        elif cells[3] == cells[4] and cells[4] == cells[5] and cells[0] != 0:
            winning_player = cells[3]
        elif cells[6] == cells[7] and cells[7] == cells[8] and cells[0] != 0:
            winning_player = cells[6]
        elif all(cells):
            winning_player = 3

    clear = False
    pygame.display.flip()

    dt = clock.tick(60) / 1000

    if winning_player == 1 or winning_player == 1:
        print(f"Player {winning_player} is the winner!")
        break
    elif winning_player == 3:
        print("It's a tie!")
        break

pygame.quit()
