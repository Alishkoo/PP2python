import pygame as pg
import sys

class Gun():
    #инициализация
    def __init__(self,screen):
        self.screen = screen
        self.image = pg.image.load("D:\PP2python\mygame\images\pixil-frame-0 (2).png")
        self.rect = self.image.get_rect() # позиция амонга брат
        self.screen_rect = screen.get_rect() # позиция экрана 
        self.rect.centerx = self.screen_rect.centerx # центр амонга боже
        self.center = float(self.rect.centerx) # чтобы она могла принимать не целые числа 
        self.rect.bottom = self.screen_rect.bottom # низ экрана
        self.mright = False
        self.mleft = False


    def printing(self):
        #draw the gun
        self.screen.blit(self.image, self.rect)


    def update_gun(self):
        #обновление позиции пушки
        if self.mright == True and self.rect.right < self.screen_rect.right:
            self.center += 0.7
        
        elif self.mleft == True and self.rect.left > self.screen_rect.left:
            self.center -= 0.7
    

        self.rect.centerx = self.center


