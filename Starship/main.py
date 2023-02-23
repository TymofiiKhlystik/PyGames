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
score = 0

WIDTH, HEIGHT, = info.current_w, info.current_h
# Images
background = pg.image.load("images/fon 2.jpg")
meteors_images = ({"path": "meteor main.png", "score": 5}, {"path": "meteor black.png", "score": 4},
                  {"path": "meteoritt.png", "score": 2}, {"path": "fiery meteor1.png", "score": 2},
                  {"path": "fiery meteor.png", "score": 4}, {"path": "meteor white.png", "score": 3})
meteors_surf = [pg.image.load("images/" + path["path"]) for path in meteors_images]

SP = sp.Spaceship(WIDTH // 2, HEIGHT - 100, speed, WIDTH)

ARIAL_FOND_PATH = pg.font.match_font("arial")
ARIAL_FOND_54 = pg.font.Font(ARIAL_FOND_PATH, 54)
ARIAL_FOND_60 = pg.font.Font(ARIAL_FOND_PATH, 60)

boom_meteor = pg.mixer.Sound("sounds/boom.ogg")
boom_space = pg.mixer.Sound("sounds/boom_space.ogg")
sound_laser = pg.mixer.Sound("sounds/laser.ogg")


def create_meteor(grope):
    index = randint(0, len(meteors_images) - 1)
    x = randint(30, WIDTH - 30)
    speed1 = randint(1, 5)

    return Meteor(x, speed1, meteors_surf[index], meteors_images[index]["score"], grope)


def collide_spaceship():
    global game_over
    for meteor in meteors:
        if SP.rect.collidepoint(meteor.rect.center):
            boom_space.play()
            game_over = True
            meteor.kill()


def collide_bullet():
    global score
    for bull in bullet_group:
        for meteor in meteors:
            if meteor.rect.collidepoint(bull.rect.center):
                boom_meteor.play()
                score += meteor.score
                meteor.kill()
                bull.kill()
                print(score)


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
                    sound_laser.play()
            if event.key == pg.K_r:
                game_over = False
                score = 0
                for m in meteors:
                    m.kill()
                SP = sp.Spaceship(WIDTH // 2, HEIGHT - 100, speed, WIDTH)

        if event.type == pg.USEREVENT:
            create_meteor(meteors)
    screen.blit(background, (0, 0))
    meteors.draw(screen)
    score_surface = ARIAL_FOND_54.render(str(score), True, WHITE)
    screen.blit(score_surface, [10, 15])
    if not game_over:
        screen.blit(score_surface, [10, 15])
        screen.blit(SP.image, SP.rect)
        SP.update(WIDTH)
        collide_spaceship()
        collide_bullet()
    else:
        retry_surface = ARIAL_FOND_60.render("press \"R\" to restart", True, WHITE)
        screen.blit(retry_surface, [WIDTH//2 - retry_surface.get_width()//2, HEIGHT//2])
    bullet_group.draw(screen)
    pg.display.update()
    bullet_group.update()
    clock.tick(FPS)
    meteors.update(HEIGHT)
