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
    if second < 10 and minute < 10:
        show_time = Font.render(str(hour) + ":0" + str(minute) + ":0" + str(second), True, (0, 0, 0))
    elif second < 10:
        show_time = Font.render(str(hour) + ":" + str(minute) + ":0" + str(second), True, (0, 0, 0))
    elif minute < 10:
        show_time = Font.render(str(hour) + ":0" + str(minute) + ":" + str(second), True, (0, 0, 0))
    else:
        show_time = Font.render(str(hour) + ":" + str(minute) + ":" + str(second), True, (0, 0, 0))

    screen.blit(show_time, (15, 15))


def draw_seconds():
    # every second move 6 degrees right
    # 4/5 shortens arm length
    # 300 is the radius. no clue what the other 300 does but it doesn't work without it
    x = 300 * (4 / 5) * math.cos(math.radians(90 - second * 6)) + 300
    y = 300 * (4 / 5) * math.sin(-math.radians(90 - second * 6)) + 300
    pg.draw.line(screen, (255, 0, 0), (300, 300), (x, y), 2)


def draw_minutes():
    # every minute move 6 degrees right
    x = 300 * (4 / 5) * math.cos(math.radians(90 - minute * 6)) + 300
    y = 300 * (4 / 5) * math.sin(-math.radians(90 - minute * 6)) + 300
    pg.draw.line(screen, (0, 0, 0), (300, 300), (x, y), 5)


def draw_hours():
    # every hour move 30 degrees right
    x = 300 * (3 / 5) * math.cos(math.radians(90 - hour * 30)) + 300
    y = 300 * (3 / 5) * math.sin(-math.radians(90 - hour * 30)) + 300
    pg.draw.line(screen, (0, 0, 0), (300, 300), (x, y), 10)


def draw_time():
    draw_seconds()
    draw_minutes()
    draw_hours()
