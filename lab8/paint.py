import pygame
import sys

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
    
    drawRect = True
    drawCircle = False
    eraser = False
    while True:
        pressed = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    color = WHITE
                if event.key == pygame.K_2:
                    color = RED
                if event.key == pygame.K_3:
                    color = BLUE
                if event.key == pygame.K_4:
                    color = YELLOW
                if event.key == pygame.K_5:
                    color = GREEN
                if event.key == pygame.K_q:
                    drawRect = True
                    drawCircle = False
                    eraser = False
                if event.key == pygame.K_w:
                    drawRect = False
                    drawCircle = True
                    eraser = False
                if event.key == pygame.K_e:
                    drawRect = False
                    drawCircle = False
                    eraser = True
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
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and drawRect:
            #если закоментить нижний код, то можно понять зачем нужен baselayer
            screen.blit(baseLayer, (0, 0))
            r = calculateRect(prevX, prevY, currentX, currentY)
            pygame.draw.rect(screen, color, pygame.Rect(r), 1)
        #тот же самый вывод но только для круга
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and drawCircle:
            screen.blit(baseLayer, (0, 0))
            r = calculateRect(prevX, prevY, currentX, currentY)
            #pygame.draw.circle(screen, color, (abs(prevX - currentX) / 2, abs(prevY - currentY) / 2), )
            pygame.draw.ellipse(screen, color, r, 1)
        mouse = pygame.mouse.get_pos()
        if eraser and pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, (0, 0, 0), mouse, 25)
            
        pygame.display.flip()
        clock.tick(60)
            
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    
    
main()