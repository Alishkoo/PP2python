import pygame
import sys


def run():
    pygame.init() #инициализация
    screen = pygame.display.set_mode((612,357)) #создаем экран
    pygame.display.set_caption("Game") #название экрану

    #создаем часы 
    clock = pygame.time.Clock()

    # создаем иконку, загружая фото 
    icon = pygame.image.load("D:\PP2python\game\images\logo.png").convert_alpha()
    pygame.display.set_icon(icon)

    #создаем пулю

    bullet = pygame.image.load("D:/PP2python/game/images/bullet.png").convert_alpha()

    #Создаем квадрат и рисуем чтобы могли выводить
    square = pygame.Surface((50, 70))
    square.fill('Blue')

    #Создаем шрифт, текст
    myfont = pygame.font.Font("D:\PP2python\game\myfont\Roboto-Medium.ttf", 40)
    text_you_lose = myfont.render("You lose!", False, (193, 196, 199))
    text_restart = myfont.render("Restart Game", False, (115, 132, 148))
    text_restart_rect = text_restart.get_rect(topleft=(200, 200))

    #Создаем бэкграунд, вставляем в экран, когда игрок стоит 
    player = pygame.image.load("D:/PP2python/game/images/player_right/right1.png").convert_alpha()
    bg = pygame.image.load('D:/PP2python/game/images/bg.jpg').convert_alpha()

    #создаем врага 
    enemy = pygame.image.load("D:\PP2python\game\images\enemy.png").convert_alpha()
    enemy_x = 612
    enemy_y = 260

    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, 2500)

   
    #переменные для передвижение игрока 
    player_x = 150
    player_speed = 5
    player_y = 250

    is_jump = False
    high_jump = 8

    #создаем лист для анимации игрока
    walk_right = [
        pygame.image.load("D:/PP2python/game/images/player_right/right1.png").convert_alpha(),
        pygame.image.load("D:/PP2python/game/images/player_right/right2.png").convert_alpha(),
        pygame.image.load("D:/PP2python/game/images/player_right/right3.png").convert_alpha(), 
        pygame.image.load("D:/PP2python/game/images/player_right/right4.png").convert_alpha()
    ]
    walk_left = [
        pygame.image.load("D:\PP2python\game\images\player_left\left1.png").convert_alpha(),
        pygame.image.load("D:\PP2python\game\images\player_left\left2.png").convert_alpha(),
        pygame.image.load("D:\PP2python\game\images\player_left\left3.png").convert_alpha(), 
        pygame.image.load("D:\PP2python\game\images\player_left\left4.png").convert_alpha()
    ]

    player_anim_count = 0
    #координаты заднего фона, для анимации
    bg_x = 0

    #звук для заднего фона
    #bg_music = pygame.mixer.Sound("name of music")

    #списки для врагов и пуль

    enemy_list = []
    bullets = []
    bullets_left = 3

    gameplay = True

    while True:

        # screen.fill((114, 157, 224))

        # отображение на экране с позициями
        # screen.blit(square, (0, 0))

        #отображение текста
        # screen.blit(text_surface, (150, 150))

        #другой метод рисовать предметы на экране
        # pygame.draw.circle(screen, 'Red', (50, 150), 30)


        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 612, 0))
        screen.blit(bg, (bg_x - 612, 0))
        
        if gameplay:
            

            #отображение сколько пуль осталось 
            if bullets_left == 3:
                screen.blit(bullet, (570, 30))
                screen.blit(bullet, (540, 30))
                screen.blit(bullet, (510, 30))
            elif bullets_left == 2:
                screen.blit(bullet, (570, 30))
                screen.blit(bullet, (540, 30))
            elif bullets_left == 1:
                screen.blit(bullet, (570, 30))



            #фигуры для игрока и врагов
            player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))
            # enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))
            
            # движение врагов
            #список врагов 
            # if enemy_list:
            #     for (i ,el) in enumerate(enemy_list):
            #         screen.blit(enemy, el)
            #         el.x -= 10

            #         if el.x < -10:
            #             enemy_list.pop(i)

            #         if player_rect.colliderect(el):
            #             gameplay = False

            

            #движение игрока
            keys = pygame.key.get_pressed()


            #создание снарядов 
            if keys[pygame.K_l]:
                pass
            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x, el.y))
                    el.x += 8
                    
                    if el.x >= 630:
                        bullets.pop(i)

                    if enemy_list:
                        for (index, enemy_el) in enumerate(enemy_list):
                            if el.colliderect(enemy_el):
                                bullets.pop(i)
                                enemy_list.pop(index)

            #стороны анимации 
            if keys[pygame.K_a]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
                bg_x += 5
                if bg_x >= 612:
                    bg_x = 0
            elif keys[pygame.K_d]:
                bg_x -= 5
                if bg_x <= -612:
                    bg_x = 0
                screen.blit(walk_right[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_right[0], (player_x, player_y))


            #влево
            if keys[pygame.K_d] and player_x <= 540:
                player_x += player_speed
            # вправо 
            elif keys[pygame.K_a] and player_x >= 50:
                player_x -= player_speed
            
            #реализация прыжка
            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if high_jump >= -8:
                    if high_jump > 0:
                        player_y -= (high_jump ** 2) / 2
                    else:
                        player_y += (high_jump ** 2) / 2
                    high_jump -= 1
                else:
                    is_jump = False
                    high_jump = 8


            #отвечает за анимацию
            player_anim_count += 1
            player_anim_count = player_anim_count % 4


        else:
            screen.fill((87, 88, 89))
            screen.blit(text_you_lose, (230, 150))
            screen.blit(text_restart, (200, 200))

            mouse = pygame.mouse.get_pos()
            if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player_x = 150
                player_y = 250
                enemy_list.clear()
                bullets.clear()
                bullets_left = 3


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == enemy_timer:
                enemy_list.append(enemy.get_rect(topleft=(enemy_x, enemy_y)))
            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_l and bullets_left > 0:
                bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y + 10)))
                bullets_left -= 1
                


        clock.tick(15)

run()