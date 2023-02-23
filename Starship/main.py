import pygame as pg
from meteor import Meteor
import spaceship as sp
from random import randint

pg.init()
clock = pg.time.Clock()
pg.time.set_timer(pg.USEREVENT, 1000)
info = pg.display.Info()
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
speed = 10

WIDTH, HEIGHT, = info.current_w, info.current_h
background = pg.image.load("images/fon 2.jpg")

meteors_images = ({"path": "meteor main.png", "score": 10}, {"path": "meteor black.png", "score": 8},
                  {"path": "meteoritt.png", "score": 6}, {"path": "fiery meteor1.png", "score": 5},
                  {"path": "fiery meteor.png", "score": 9}, {"path": "meteor white.png", "score": 7})
meteors_surf = [pg.image.load("images/" + path["path"]) for path in meteors_images]

SP = sp.Spaceship(WIDTH // 2, HEIGHT - 100, speed, WIDTH)


def create_meteor(grope):
    index = randint(0, len(meteors_images) - 1)
    x = randint(30, WIDTH - 30)
    speed1 = randint(1, 5)

    return Meteor(x, speed1, meteors_surf[index], meteors_images[index]["score"], grope)


def collide_spaceship():
    global game_over
    for meteor in meteors:
        if SP.rect.collidepoint(meteor.rect.center):
            game_over = True
            meteor.kill()


spaceship_group = pg.sprite.Group()
meteors = pg.sprite.Group()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("METEOR")

bullet_group = pg.sprite.Group()

create_meteor(meteors)
meteorite = create_meteor(meteors)

game_over = False
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()
            if event.key == pg.K_SPACE:
                if not game_over:
                    bullet_group.add(SP.create_bullet())
        if event.type == pg.USEREVENT:
            create_meteor(meteors)
    screen.blit(background, (0, 0))
    meteors.draw(screen)

    if not game_over:
        screen.blit(SP.image, SP.rect)
        SP.update(WIDTH)
        collide_spaceship()

    bullet_group.draw(screen)
    pg.display.update()
    bullet_group.update()
    clock.tick(FPS)
    meteors.update(HEIGHT)
