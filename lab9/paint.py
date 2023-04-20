import pygame
import sys
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    
    WHITE = (255, 255, 255)
    RED = (255,0,0)
    BLUE = (0,0,255)
    YELLOW = (255,255,0)
    GREEN = (124,252,0)
    
    #цвет
    color = WHITE
    #для временного показывания результата
    baseLayer = pygame.Surface((640, 480))
    
    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
    
    screen.fill((0, 0, 0))
    
    isMouseDown = False
    
    #создаю список для хранения значений инструментов
    drawRect = True
    drawCircle = False
    drawSquare = False
    draw_eq_triangle = False
    draw_right_triangle = False
    draw_rhombus = False
    eraser = False
    tools = [True, False, False, False, False, False, False]
    while True:
        pressed = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    color = WHITE
                if event.key == pygame.K_w:
                    color = RED
                if event.key == pygame.K_e:
                    color = BLUE
                if event.key == pygame.K_r:
                    color = YELLOW
                if event.key == pygame.K_t:
                    color = GREEN
                if event.key == pygame.K_1:
                    # drawRect = True
                    for i in range(0, len(tools)):
                        if i == 0:
                            tools[i] = True
                        else:
                            tools[i] = False
                if event.key == pygame.K_2:
                    
                    # drawCircle = True
                    
                    for i in range(0, len(tools)):
                        if i == 1:
                            tools[i] = True
                        else:
                            tools[i] = False
                if event.key == pygame.K_3:
                    #square
                    for i in range(0, len(tools)):
                        if i == 2:
                            tools[i] = True
                        else:
                            tools[i] = False
                if event.key == pygame.K_4:
                    #eq_triangle
                    for i in range(0, len(tools)):
                        if i == 3:
                            tools[i] = True
                        else:
                            tools[i] = False
                if event.key == pygame.K_5:
                    #right_triangle
                    for i in range(0, len(tools)):
                        if i == 4:
                            tools[i] = True
                        else:
                            tools[i] = False   
                if event.key == pygame.K_6:
                    #rhombus
                    for i in range(0, len(tools)):
                        if i == 5:
                            tools[i] = True
                        else:
                            tools[i] = False           
                if event.key == pygame.K_7:
                    #eraser = True
                    for i in range(0, len(tools)):
                        if i == 6:
                            tools[i] = True
                        else:
                            tools[i] = False
            #при нажатии правой кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                #берем координаты начала и последней
                if event.button == 1:
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currectY = event.pos[1]
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]
                
                    
            #когда отпускает
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))
      
            #когда мышка двигается
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
                
        #это вывод временного квадратика чтобы пользователь видел как изменяется размер квадратика и куда он нарисуется     
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and tools[0]:
            #если закоментить нижний код, то можно понять зачем нужен baselayer
            screen.blit(baseLayer, (0, 0))
            r = calculateRect(prevX, prevY, currentX, currentY)
            pygame.draw.rect(screen, color, pygame.Rect(r), 1)
        #тот же самый вывод но только для круга
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and tools[1]:
            screen.blit(baseLayer, (0, 0))
            r = calculateRect(prevX, prevY, currentX, currentY)
            #pygame.draw.circle(screen, color, (abs(prevX - currentX) / 2, abs(prevY - currentY) / 2), )
            pygame.draw.ellipse(screen, color, r, 1)
        #для квадрата
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and tools[2]:
            screen.blit(baseLayer, (0, 0))
            s = calculateSquare(prevX, prevY, currentX, currentY)
            pygame.draw.rect(screen, color, s, 1)
        #для равностороннего треугольника
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and tools[3]:
            screen.blit(baseLayer, (0, 0))
            t = calculateEqTriangle(prevX, prevY, currentX, currentY)
            pygame.draw.polygon(screen, color, t, 1)
        #для прямого треугольника
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and tools[4]:
            screen.blit(baseLayer, (0, 0))
            t = calculateRightTriangle(prevX, prevY, currentX, currentY)
            pygame.draw.polygon(screen, color, t, 1)
        #для ромба
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and tools[5]:
            screen.blit(baseLayer, (0, 0))
            t = calculateDiamond(prevX, prevY, currentX, currentY)
            pygame.draw.polygon(screen, color, t, 1)
        mouse = pygame.mouse.get_pos()
        if tools[6] and pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, (0, 0, 0), mouse, 25)
            
        pygame.display.flip()
        clock.tick(60)
        
        # print(tools)
            
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


def calculateSquare(x1, y1, x2, y2):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    x = min(x1, x2)
    y = min(y1, y2)
    size = min(width, height)
    
    
    return pygame.Rect(x, y, size, size)


def calculateEqTriangle(x1, y1, x2, y2):
    # Определение координат вершин треугольника
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    x = min(x1, x2)
    y = min(y1, y2)
    
    side_length = min(width, height)
    triangle_height = side_length * math.sqrt(3) / 2
    x1 = x + (width - side_length) // 2
    y1 = y + height - triangle_height
    x2 = x1 + side_length
    y2 = y1
    x3 = x + width // 2
    y3 = y1 - triangle_height
    
    return [(x1, y1), (x2, y2), (x3, y3)]


def calculateRightTriangle(x1, y1, x2, y2):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    #задаю начальные координаты прямого треугольника
    x = min(x1, x2)
    y = min(y1, y2)
    
    #возвращаю координаты прямого треугольника
    if x2 < x1 and y2 < y1:
        return [(x1, y1), (x1, y2), (x2, y1)]
    
    elif x2 > x1 and y1 > y2:
        return [(x1, y1), (x2, y1), (x1, y2)]
    
    elif x1 > x2 and y2 > y1:
        return [(x1, y1), (x2, y1), (x1, y2)]
    
    return [(x, y), (x + width, y), (x, y + height)]    


def calculateDiamond(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    
    # Определение координат центра ромба
    center_x = x + width // 2
    center_y = y + height // 2
    # Определение длины диагонали ромба
    diagonal_length = min(width, height)
    # Рисование ромба
    return [(center_x, y), (x + width, center_y), (center_x, y + height), (x, center_y)]
    
main()