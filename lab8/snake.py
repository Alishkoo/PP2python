import pygame
import sys
import random

def main():
    pygame.init()
    
    #таймер для управления фпс
    timer = pygame.time.Clock()
    
    #переменные константы пишутся с заглавной
    FRAME_COLOR = (0, 255, 204)
    WHITE = (255, 255, 255)
    BLUE = (204, 255, 255)
    HEAD_COLOR = (0, 204, 153)
    RED = (255, 0, 0)
    
    #размеры блока игрового поля и количество
    SIZE_BLOCK = 20
    COUNT_BLOCKS = 20
    
    #работаем с шрифтом загружаем
    myfont = pygame.font.SysFont('courier', 36)
    
    #цвета змеи
    SNAKE_COLOR = (0, 102, 0)
    
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Змейка")
    
    #функция для подсчета размеров блоков игрового поля
    def draw_blocks(color, column, row):
        pygame.draw.rect(screen, color, [80 + column * COUNT_BLOCKS + (column + 1), 
                                                 20 + row * COUNT_BLOCKS + (row + 1) , 
                                                 SIZE_BLOCK, 
                                                 SIZE_BLOCK])
        
        
    class SnakeBlock:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        #функция которая проверяет внутри ли змея игрового поля 
        def is_inside(self):
            return 0<= self.x < COUNT_BLOCKS and 0<= self.y < COUNT_BLOCKS
        
        #функция для сравнение совпадают ли блоки, тут self и other
        def __eq__(self, other):
            return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y
    
    
    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS - 1)
        y = random.randint(0, COUNT_BLOCKS - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
            empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
        return empty_block
    
    #змея 
    snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    #создаем еду
    apple = get_random_empty_block()
    
    #переменные для движения змейки
    d_x = 1
    d_y = 0
    speed = 1
    total = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and d_x != 0:
                    d_x = 0
                    d_y = -1
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and d_x != 0:
                    d_x = 0
                    d_y = 1
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and d_y != 0:
                    d_x = -1
                    d_y = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and d_y != 0:
                    d_x = 1
                    d_y = 0
                     
        
        screen.fill(FRAME_COLOR)
        
        #вывод игрового поля
        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (column + row) % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE
                draw_blocks(color, column, row)
        
        #вывод текста total и speed
        text_total = myfont.render(f"Total: {total}", True, WHITE)   
        text_speed = myfont.render(f"Speed: {speed}", True, WHITE)   
        screen.blit(text_speed, (300, 500))
        screen.blit(text_total, (100, 500))
        

        #проверка змея внутри или нет
        head = snake_blocks[-1]
        if not head.is_inside():
              sys.exit()
                
        #рисуем яблоко        
        draw_blocks(RED, apple.x, apple.y)
        #рисуем змею
        for block in snake_blocks:
            draw_blocks(SNAKE_COLOR, block.x, block.y)
            # block.x += d_x
            # block.y += d_y       
        
        #Реализация движения змеи, голова ([-1]) это послед элемент в списке (snake_blocks)
        #И при движении мы двигаем последний элемент(голова) туда куда нам нужно при этом удаляя первый первый элемент(хвост)
        
        new_head = SnakeBlock(head.x + d_x, head.y + d_y)
        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        
        #так как и голова и яблоко являются одним и тем же классом у них сравниваются все данные в том числе и координаты 
        if head == apple:
            total += 1
            speed = total // 2 + 1 #ускоряем каждые 2 сьеденных яблок
            snake_blocks.append(apple)
            apple = get_random_empty_block()
        
        pygame.display.update()
        timer.tick(4 + speed)
        
        
main()