import pygame
import sys

bg = pygame.image.load("D:/PP2python/another_game/images/1589896354.jpg")

# Класс, описывающий поведение главного игрока
class Player(pygame.sprite.Sprite):
    # Изначально игрок смотрит вправо, поэтому эта переменная True
    right = True

    def __init__(self):
        #вызываем конструктор 
        #так же вызываем конструктор родительского класса
        super().__init__()

        #создаем фото персонажа 
        self.image = pygame.image.load("D:/PP2python/another_game/images/right1.png")

        #создаем фигуру для персонажа
        self.rect = self.image.get_rect()

        #векторы скорости персонажа
        self.change_x = 0
        self.change_y = 0

    def 



def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("2D")
   
    
    while True:
        screen.blit(bg, (0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        
        
main()