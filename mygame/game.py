import sys
import pygame as pg
from gun import Gun
import control 
from pygame.sprite import Group



def run():

    pg.init()
    screen = pg.display.set_mode((800,700))
    pg.display.set_caption("Game")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    control.create_army(screen, inos)

    while True:
        control.events(screen, gun, bullets)
        gun.update_gun()
        control.update(bg_color, screen, gun, inos, bullets)
        control.update_bullets(bullets)


run()