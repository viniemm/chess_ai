import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True
pygame.display.set_caption("Chess AI")

width, height = 100, 100

bpawn   = pygame.transform.scale(pygame.image.load("assets/bpawn.png"), (width, height))
bbishop = pygame.transform.scale(pygame.image.load("assets/bbishop.png"), (width, height))
bqueen  = pygame.transform.scale(pygame.image.load("assets/bqueen.png"), (width, height))
bhorse  = pygame.transform.scale(pygame.image.load("assets/bhorse.png"), (width, height))
brook   = pygame.transform.scale(pygame.image.load("assets/brook.png"), (width, height))
bking   = pygame.transform.scale(pygame.image.load("assets/bking.png"), (width, height))
wpawn   = pygame.transform.scale(pygame.image.load("assets/wpawn.png"), (width, height))
wbishop = pygame.transform.scale(pygame.image.load("assets/wbishop.png"), (width, height))
wqueen  = pygame.transform.scale(pygame.image.load("assets/wqueen.png"), (width, height))
whorse  = pygame.transform.scale(pygame.image.load("assets/whorse.png"), (width, height))
wrook   = pygame.transform.scale(pygame.image.load("assets/wrook.png"), (width, height))
wking   = pygame.transform.scale(pygame.image.load("assets/wking.png"), (width, height))

default_pos = {
    "brook_1"  : [0, 0],
    "bhorse_1" : [1, 0],
    "bbishop_1": [2, 0],
    "bqueen"   : [3, 0],
    "bking"    : [4, 0],
    "bbishop_2": [5, 0],
    "bhorse_2" : [6, 0],
    "brook_2"  : [7, 0],

    "wrook_1"  : [0, 7],
    "whorse_1" : [1, 7],
    "wbishop_1": [2, 7],
    "wqueen"   : [3, 7],
    "wking"    : [4, 7],
    "wbishop_2": [5, 7],
    "whorse_2" : [6, 7],
    "wrook_2"  : [7, 7],
}

for y in range(0, 8):
    for x in range(0, 8):
        box = pygame.Rect(0 + 100 * x, 0 + 100 * y, 100, 100)
        if (x + y) % 2 == 0:
            pygame.draw.rect(screen, (255, 255, 255), box)

while running:
    screen.blit(brook,   (default_pos["brook_1"  ][0]*100, default_pos["brook_1"  ][1]*100))
    screen.blit(bhorse,  (default_pos["bhorse_1" ][0]*100, default_pos["bhorse_1" ][1]*100))
    screen.blit(bbishop, (default_pos["bbishop_1"][0]*100, default_pos["bbishop_1"][1]*100))
    screen.blit(bqueen,  (default_pos["bqueen"   ][0]*100, default_pos["bqueen"   ][1]*100))
    screen.blit(bking,   (default_pos["bking"    ][0]*100, default_pos["bking"    ][1]*100))
    screen.blit(bbishop, (default_pos["bbishop_2"][0]*100, default_pos["bbishop_2"][1]*100))
    screen.blit(bhorse,  (default_pos["bhorse_2" ][0]*100, default_pos["bhorse_2" ][1]*100))
    screen.blit(brook,   (default_pos["brook_2"  ][0]*100, default_pos["brook_2"  ][1]*100))
    for i in range(0, 8):
        screen.blit(bpawn, (i*100, 100))
        screen.blit(wpawn, (i*100, 600))

    screen.blit(wrook,   (default_pos["wrook_1"  ][0]*100, default_pos["wrook_1"  ][1]*100))
    screen.blit(whorse,  (default_pos["whorse_1" ][0]*100, default_pos["whorse_1" ][1]*100))
    screen.blit(wbishop, (default_pos["wbishop_1"][0]*100, default_pos["wbishop_1"][1]*100))
    screen.blit(wqueen,  (default_pos["wqueen"   ][0]*100, default_pos["wqueen"   ][1]*100))
    screen.blit(wking,   (default_pos["wking"    ][0]*100, default_pos["wking"    ][1]*100))
    screen.blit(wbishop, (default_pos["wbishop_2"][0]*100, default_pos["wbishop_2"][1]*100))
    screen.blit(whorse,  (default_pos["whorse_2" ][0]*100, default_pos["whorse_2" ][1]*100))
    screen.blit(wrook,   (default_pos["wrook_2"  ][0]*100, default_pos["wrook_2"  ][1]*100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface = pygame.Surface((100, 100), pygame.SRCALPHA)

    pygame.display.flip()
