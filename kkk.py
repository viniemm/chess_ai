import os, sys
import pygame as pg  # lazy but responsible (avoid namespace flooding)


class Character:
    def __init__(self, rect):
        IMAGE = pg.image.load("assets/bbishop.png").convert()  # or .convert_alpha()
        # Create a rect with the size of the image.
        recta = IMAGE.get_rect()
        recta.center = (200, 300)
        self.rect = recta
        self.click = False
        self.image = pg.Surface(self.rect.size).convert()
        # self.image.fill((255, 0, 0))

    def update(self, surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image, self.rect)


def main(Surface, Player):
    game_event_loop(Player)
    Surface.fill(0)
    Player.update(Surface)


def game_event_loop(Player):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if Player.rect.collidepoint(event.pos):
                Player.click = True
        elif event.type == pg.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pg.QUIT:
            pg.quit();
            sys.exit()


if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1000, 600))
    MyClock = pg.time.Clock()
    MyPlayer = Character()
    MyPlayer.rect.center = Screen.get_rect().center
    while 1:
        main(Screen, MyPlayer)
        pg.display.update()
        MyClock.tick(60)
