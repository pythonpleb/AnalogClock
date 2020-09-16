import pygame as pg
from window import set_window
from graphics import draw_clock, get_time_digital, draw_time


running = True


def events():
    global running
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False


def main():
    events()
    set_window()
    draw_clock()
    get_time_digital()
    draw_time()
    pg.display.update()


if __name__ == '__main__':
    while running:
        main()
    pg.quit()
