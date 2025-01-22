import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.line(screen, "white", ((screen.get_width() / 3), 0),
                     ((screen.get_width() / 3), screen.get_height()), width=5)
    pygame.draw.line(screen, "white", (((screen.get_width() * 2) / 3), 0),
                     (((screen.get_width() * 2) / 3), screen.get_height()), width=5)
    pygame.draw.line(screen, "white", (0, (screen.get_height() / 3)),
                     (screen.get_width(), (screen.get_height() / 3)), width=5)
    pygame.draw.line(screen, "white", (0, ((screen.get_height() * 2) / 3)),
                     (screen.get_width(), ((screen.get_height() * 2) / 3)), width=5)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
