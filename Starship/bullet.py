import pygame as pg


class Bullet(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/bullet.png")
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0 - 50:
            self.kill()




