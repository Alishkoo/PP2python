import pygame as pg
import sys

class Bullet(pg.sprite.Sprite):
    def __init__(self, screen, gun):
        #создаем пулю там где стоит пушка по этому ее и передали
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(0, 0, 4, 14)
        self.color = 255, 0, 0
        self.speed = 1.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)


    def update(self):
        #обновление пули когда она движется
        self.y -= self.speed
        self.rect.y = self.y


    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect)


    