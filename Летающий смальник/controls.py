import pygame as pg
import sys


def event(smile):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            if event.key == pg.K_w:
                smile.rect.y -= 10
            if event.key == pg.K_s:
                smile.rect.y += 10
            if event.key == pg.K_a:
                smile.rect.x -= 10
            if event.key == pg.K_d:
                smile.rect.x += 10