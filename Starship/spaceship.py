import pygame as pg
import bullet


class Spaceship(pg.sprite.Sprite):
    """x, y - coordinates Spaceship
    filename - path to the image
    speed - speed coordinates 'x'
    width - width screen"""

    def __init__(self, x, y, speed, width):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/spaceship-png-icon-17260.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.width = width

    def update(self, *args):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > self.width-self.rect.width:
                self.rect.x = self.width-self.rect.width
        if keys[pg.K_SPACE]:
            pass

    def create_bullet(self):
        return bullet.Bullet(self.rect.centerx, self.rect.y)

