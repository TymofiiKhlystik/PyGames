import pygame as pg
from random import randint

pg.init()

WIDTH, HEIGHT = 840, 560
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
FPS = 3
score = 0
start_pos_circle = randint(0, WIDTH), randint(0, HEIGHT)

alive = True
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BLACK)

    pg.draw.circle(screen, RED, start_pos_circle, CIRCLE)
    pg.display.update()
    clock.tick(FPS)
