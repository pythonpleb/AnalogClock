import pygame as pg

width = 600
height = 600
screen = pg.display.set_mode((width, height))


def set_window():
    # set window caption
    screen.fill((255, 255, 255))
    pg.display.set_caption('Analog Clock')

    # add clock image here
    analog_icon = pg.image.load('clock_icon.png')
    pg.display.set_icon(analog_icon)
