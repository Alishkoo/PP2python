import pygame
import sys
from random import random, randrange, randint

def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((434, 626))
    bg = pygame.image.load("D:/PP2python/lab8/car_game/images/background.png").convert_alpha()
    end = pygame.image.load("D:\PP2python\lab8\car_game\images\end.png").convert_alpha()
    
    
    
    #создаем кнопки yes or no 
    myfont = pygame.font.Font("D:/PP2Python/lab8/car_game/fonts/Roboto-Medium.ttf", 40)
    text_no = myfont.render("No", False, (193, 196, 192))
    text_yes = myfont.render("Yes", False, (193, 196, 192))
    text_no_rect = text_no.get_rect(topleft=(190, 370))
    text_yes_rect = text_yes.get_rect(topleft=(190, 290))

    #создаем таймер когда будут создаваться машинки
    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, 1000)


    #player car
    player_x = 200
    player_y = 500
    car_player = pygame.transform.rotate(pygame.image.load("D:/PP2Python/lab8/car_game/images/third.png").convert_alpha(), 180)
    # car_player_rect = car_player.get_rect(topleft=(player_x, player_y))

    #создаем другой таймер для монеток
    coin_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(coin_timer, 2000)

    #создаем монетку
    coin_amount = 0
    coin_x = 290
    coin_y = 50
    coin_x_list = [90, 160, 230, 290]
    coin_y_list = [200, 100, 50, 150]
    coin = pygame.image.load("D:\PP2Python\lab8\car_game\images\money.png").convert_alpha()
    coin_rect = coin.get_rect(topleft=(coin_x, coin_y))
    coin_list = []
    
    #enemy cars
    enemy_pos_list = [90, 120, 160, 180, 230, 240, 250, 290]
    # enemy_x = enemy_pos_list[randint(0, 3)] # 80, 150, 220 , 280
    enemy_x = 90
    enemy_y = -20
    car_image_list = [
        pygame.image.load("D:/PP2Python/lab8/car_game/images/first.png").convert_alpha(),
        pygame.image.load("D:\PP2Python\lab8\car_game\images\second.png").convert_alpha(),
        pygame.image.load("D:/PP2Python/lab8/car_game/images/third.png").convert_alpha(), 
        pygame.image.load("D:/PP2Python/lab8/car_game/images/forth.png").convert_alpha()
    ]
    #car_enemy =pygame.image.load("D:/PP2Python/lab8/car_game/images/first.png").convert_alpha()
    car_enemy_rect = car_image_list[0].get_rect(topleft=(enemy_x, enemy_y))
    enemy_speed = 0.5
    enemy_list = []

    bg_y = 0
    starttime = 0

    gameplay = True
    while True:
        
        if gameplay:
            #секундомер для игры 
            ticks=pygame.time.get_ticks() - starttime
            millis=ticks%1000
            seconds=int(ticks/1000 % 60)
            text_seconds = myfont.render(f"{seconds}", True, 'dodgerblue')

            
            #рандомно задаю значения для позиции противников
            random_pos = randint(0, 7)
            #random_image = randint(0, 3)
            #монетки
            coin_x = coin_x_list[randint(0, 3)]
            coin_y = coin_y_list[randint(0, 3)]
            enemy_x = enemy_pos_list[random_pos]
            
            #обработка нажатий 
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player_x >= 85:
                player_x -= 10
            elif keys[pygame.K_d] and player_x <= 310:
                player_x += 10


            #создаю для фигуру игрока для обработки его
            car_player_rect = car_player.get_rect(topleft=(player_x, player_y))


            #анимация экрана
            screen.blit(bg, (0, bg_y))
            screen.blit(bg, (0, bg_y - 626))
            bg_y += 5
            if bg_y >= 626:
                bg_y = 0
                
            #вывод секунд
            #screen.blit(text_seconds, (0, 0))
            
            #вывод количества монеток
            text_coin = myfont.render(f"{coin_amount}", True, (255, 233, 0))
            screen.blit(text_coin, (395, 10))
            
            #вывод машины игрока
            screen.blit(car_player, (player_x, player_y))

            #вывод монеток
            if coin_list:
                for (i, el) in enumerate(coin_list):
                    screen.blit(coin, el)
                    el.y += 5
                    
                    if el.y >= 630:
                        coin_list.pop(i)
            
                    if car_player_rect.colliderect(el):
                        coin_amount += 1
                        coin_list.pop(i)
                        
                        
            # вывод противников 
            if enemy_list:
                for (i, el) in enumerate(enemy_list):
                    screen.blit(car_image_list[1], el)
                    el.y += (enemy_speed + 10)
                    # print(el.x, el.y)
                    # print(player_x, player_y)
                    if el.y >= 630:
                        enemy_list.pop(i)
                    
                    if car_player_rect.colliderect(el):
                        gameplay = False
        else:
            screen.fill((0, 0, 0))
            screen.blit(end, (-80, 170))    
            
            mouse = pygame.mouse.get_pos()
            if text_yes_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]: 
                gameplay = True
                enemy_list.clear()
                player_x = 200
                player_y = 500
                enemy_speed = 0.5
                starttime = ticks
                coin_list.clear()
                coin_amount = 0
                
            if text_no_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                sys.exit()        
                    

                
        pygame.display.update()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #добавление монеток
            if event.type == coin_timer:
                coin_list.append(coin.get_rect(topleft=(coin_x, coin_y)))
            #добавление противников
            if event.type == enemy_timer:
                enemy_list.append(car_image_list[0].get_rect(topleft=(enemy_x, enemy_y)))
            #ускорение машин с временем
            if event.type == enemy_timer:
                enemy_speed += 2




main()