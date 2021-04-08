import pygame
import copy
import paint
import chess
import sys


class Piece:
    def __init__(self, id=None, empty=True):
        self.id = id
        self.empty = empty
        self.rec = None
        self.click = False


def main():
    default_pos = {
        0: Piece("brook", False),
        1: Piece("bhorse", False),
        2: Piece("bbishop", False),
        3: Piece("bqueen", False),
        4: Piece("bking", False),
        5: Piece("bbishop", False),
        6: Piece("bhorse", False),
        7: Piece("brook", False),
        8: Piece("bpawn", False),
        9: Piece("bpawn", False),
        10: Piece("bpawn", False),
        11: Piece("bpawn", False),
        12: Piece("bpawn", False),
        13: Piece("bpawn", False),
        14: Piece("bpawn", False),
        15: Piece("bpawn", False),

        63: Piece("wrook", False),
        62: Piece("whorse", False),
        61: Piece("wbishop", False),
        60: Piece("wking", False),
        59: Piece("wqueen", False),
        58: Piece("wbishop", False),
        57: Piece("whorse", False),
        56: Piece("wrook", False),
        55: Piece("wpawn", False),
        54: Piece("wpawn", False),
        53: Piece("wpawn", False),
        52: Piece("wpawn", False),
        51: Piece("wpawn", False),
        50: Piece("wpawn", False),
        49: Piece("wpawn", False),
        48: Piece("wpawn", False),
    }

    for j in range(16, 48):
        default_pos[j] = Piece()

    print(default_pos)

    pygame.init()
    screen = pygame.display.set_mode((800, 800))

    pygame.display.set_icon(pygame.transform.scale(pygame.image.load("assets/icon.png"), (32, 32)))
    running = True
    pygame.display.set_caption("Chess AI")
    paint.init_board(screen)
    current_pos = copy.deepcopy(default_pos)
    paint.board(screen, current_pos)
    clock = pygame.time.Clock()
    click = False
    a1, a2, x1, x2, y1, y2 = None, None, None, None, None, None

    while running:
        paint.init_board(screen)
        current_pos = paint.board(screen, current_pos)

        paint.highlight(screen)
        piece, x, y = paint.get_mouse_sqr(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                a1, x1, y1 = paint.get_mouse_sqr(screen)
            elif event.type == pygame.MOUSEBUTTONUP:
                a2, x2, y2 = paint.get_mouse_sqr(screen)
                clicked = False
        if a1 != None and a2 != None:
            if a1 != a2 and current_pos[a1].empty is not True:
                current_pos[a2] = current_pos[a1]
                current_pos[a1] = Piece()
            a1, a2, x1, x2, y1, y2 = None, None, None, None, None, None

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
