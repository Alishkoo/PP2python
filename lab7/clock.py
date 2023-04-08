import pygame
import sys
import datetime
def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Clock")
    bg = pygame.image.load("D:\PP2python\lab7\images\clock\clock_ready.png").convert_alpha()
    #создаю руки
    arm1 = pygame.image.load("D:/PP2python/lab7/images/clock/arm1_ready.png").convert_alpha()
    arm2 = pygame.image.load("D:/PP2python/lab7/images/clock/arm2_ready.png").convert_alpha()
    #arm1.fill((0, 0, 0))
    
    #sec = datetime.datetime.now().second
    #min = datetime.datetime.now().minute
    
    #angle = -(min * 6)
    #angle1 = 
    while True:
        sec = datetime.datetime.now().second
        min = datetime.datetime.now().minute
        
        angle = -(min * 6)
        angle1 = -(sec * 6)
        
        screen.blit(bg, (0,0))
        rotated_image_1 = pygame.transform.rotate(arm1, angle)
        rotated_image_2 = pygame.transform.rotate(arm2, angle1)
        
        screen.blit(rotated_image_1, (350 - int(rotated_image_1.get_width() / 2),350 - int(rotated_image_1.get_width() / 2)))
        screen.blit(rotated_image_2, (350 - int(rotated_image_2.get_width() / 2),350 - int(rotated_image_2.get_width() / 2)))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    
main()