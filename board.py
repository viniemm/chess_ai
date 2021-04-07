import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for y in range(0,8):
        for x in range(0,8):
            box = pygame.Rect(0 + 100 * x, 0 + 100 * y, 100, 100)
            if (x+y)%2==0:
                pygame.draw.rect(screen, (255, 255, 255), box)
    pygame.display.flip()