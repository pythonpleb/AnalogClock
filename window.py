import pygame as pg

width = 600
height = 600
screen = pg.display.set_mode((width, height))


def set_window():
    screen.fill((255, 255, 255))
    pg.display.set_caption('Analog Clock')
    # add clock image here
    # analogIcon = pg.image.load('ikon.png')
    # pg.display.set_icon(analogIcon)s
