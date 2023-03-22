import pygame as pg

class Ino(pg.sprite.Sprite):
    
    def __init__(self, screen):
        #инициализация и позиция
        super(Ino, self).__init__()

        self.screen = screen
        self.image = pg.image.load("D:\PP2python\mygame\images\pixil-frame-0 (1).png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw(self):
        #draw the ino
        self.screen.blit(self.image, self.rect)

