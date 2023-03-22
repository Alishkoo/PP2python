import pygame as pg
import sys
from bullet import Bullet
from grib import Ino

def events(screen, gun, bullets):
    for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            

            elif event.type == pg.KEYDOWN:
                #вправо
                if event.key == pg.K_d:
                    gun.mright = True
                #влево
                elif event.key == pg.K_a:
                    gun.mleft = True
                #пробел стрельба
                elif event.key == pg.K_SPACE:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)

            
            elif event.type == pg.KEYUP:
                #вправо
                if event.key == pg.K_d:
                    gun.mright = False
                #влево
                elif event.key == pg.K_a:
                     gun.mleft = False
            
#обновляет картину 
def update(bg_color, screen, gun, inos, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.printing()# рисуем пушк
    inos.draw(screen) # рисуем гриб
    pg.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_army(screen, inos):
    #создает армию
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_x = int((800 - 2 * ino_width) / ino_width)

    for ino_number in range(number_x):
        ino = Ino(screen)
        ino.x = ino_width + ino_width * ino_number
        ino.rect.x = ino.x
        inos.add(ino)

          