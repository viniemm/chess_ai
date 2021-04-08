import pygame
import math

width, height = 100, 100
pieces = {
    "bpawn": pygame.transform.scale(pygame.image.load("assets/bpawn.png"), (width, height)),
    "bbishop": pygame.transform.scale(pygame.image.load("assets/bbishop.png"), (width, height)),
    "bqueen": pygame.transform.scale(pygame.image.load("assets/bqueen.png"), (width, height)),
    "bhorse": pygame.transform.scale(pygame.image.load("assets/bhorse.png"), (width, height)),
    "brook": pygame.transform.scale(pygame.image.load("assets/brook.png"), (width, height)),
    "bking": pygame.transform.scale(pygame.image.load("assets/bking.png"), (width, height)),
    "wpawn": pygame.transform.scale(pygame.image.load("assets/wpawn.png"), (width, height)),
    "wbishop": pygame.transform.scale(pygame.image.load("assets/wbishop.png"), (width, height)),
    "wqueen": pygame.transform.scale(pygame.image.load("assets/wqueen.png"), (width, height)),
    "whorse": pygame.transform.scale(pygame.image.load("assets/whorse.png"), (width, height)),
    "wrook": pygame.transform.scale(pygame.image.load("assets/wrook.png"), (width, height)),
    "wking": pygame.transform.scale(pygame.image.load("assets/wking.png"), (width, height))
}

def init_board(screen):
    for y in range(0, 8):
        for x in range(0, 8):
            box = pygame.Rect(0 + 100 * x, 0 + 100 * y, 100, 100)
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, (255,206,158), box)
            else:
                pygame.draw.rect(screen, (209,139,71), box)


def x_val(a):
    return (a%8)*100

def y_val(b):
    return (b//8)*100


def board(screen, pos: dict) -> dict:
    res = True
    for i in range(0, 64):
        if not pos[i].empty:
            p = pieces[pos[i].id].get_rect(topleft=[x_val(i), y_val(i)])
            screen.blit(pieces[pos[i].id], p)
            pos[i].rec = p
        pass
    return pos

def get_mouse_sqr(screen):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x, y = mouse_pos[0], mouse_pos[1]
    x /= 100
    y /= 100
    x, y = math.floor(x), math.floor(y)
    a = (8*y)+x
    return a, x, y

def highlight(screen):
    a, x, y = get_mouse_sqr(screen)
    rect = (x * 100, y * 100, 100, 100)
    pygame.draw.rect(screen, (255, 0, 0, 50), rect, 5)