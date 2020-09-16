import pygame as pg
from window import screen
import datetime as dt
import math

pg.init()

Font = pg.font.Font('arial.ttf', 30)

hour = 0
minute = 0
second = 0


def draw_clock():
    pos = 0, 0
    # draw the clock img
    clock = pg.image.load('clock.png').convert_alpha()
    clock = pg.transform.scale(clock, (600, 600))
    screen.blit(clock, pos)


def get_time_digital():
    global hour
    global minute
    global second
    now = dt.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    # show current time digitally on the screen
    if second < 10:
        show_time = Font.render(str(hour) + ":" + str(minute) + ":0" + str(second), True, (0, 0, 0))
    elif minute < 10:
        show_time = Font.render(str(hour) + ":0" + str(minute) + ":" + str(second), True, (0, 0, 0))
    else:
        show_time = Font.render(str(hour) + ":" + str(minute) + ":" + str(second), True, (0, 0, 0))
    screen.blit(show_time, (15, 15))


def draw_seconds():
    # every second move 6 degrees right
    x = math.cos(6)
    y = math.sin(6)
    pg.draw.line(screen, (255, 0, 0), (300, 300), (x, y), 1)
