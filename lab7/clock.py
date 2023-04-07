import pygame
import sys
import datetime
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("Clock")
    bg = pygame.image.load("D:\PP2python\lab7\images\mickeyclock.jpeg").convert_alpha()
    
    while True:
        screen.blit(bg, (-300,-100))
        
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    
main()