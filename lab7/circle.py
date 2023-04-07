import pygame 
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Game")
    
    x = 350
    y = 350
    
    while True:
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, "Red", (x, y), 25)
        
        pygame.display.update()
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and x >= 30:
            x -= 1
        if keys[pygame.K_d] and x <= 670:
            x += 1
        if keys[pygame.K_s] and y <= 670:
            y += 1
        if keys[pygame.K_w] and y >= 30:
            y -= 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_a and x >= 30:
            #         x -= 10
            #     if event.key == pygame.K_d and x <= 700:
            #         x += 10
            #     if event.key == pygame.K_s and y <= 700:
            #         y += 10
            #     if event.key == pygame.K_w and y >= 0:
            #         y -= 10
                    
        
        
main()