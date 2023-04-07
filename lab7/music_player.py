import pygame
import sys
    
    
def main():
    pygame.init()
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Music Player")
    bg = pygame.image.load("D:/PP2python/lab7/images/musicplayer/background_ready.png").convert_alpha()
    
    #пишем кнопки для начального экрана
    myfont = pygame.font.Font("D:/PP2python/car_game/fonts/Roboto-Medium.ttf", 60)
    text = myfont.render("sweater_weather_ready", False, (193, 196, 192))
    buttom_list = [
        text.get_rect(topleft=(50, 0)),
        text.get_rect(topleft=(50, 100)),
        text.get_rect(topleft=(50, 200)), 
        text.get_rect(topleft=(50, 300)),
        text.get_rect(topleft=(50, 400)),
        text.get_rect(topleft=(50, 500)),
        text.get_rect(topleft=(50, 600))
    ]
    
    #photos of the songs
    song_counter = 0
    amount_of_songs = 7
    
    song_image_list = [
        pygame.image.load("D:\PP2python\lab7\images\musicplayer\sweater_weather_ready.png").convert_alpha(),
        pygame.image.load("D:\PP2python\lab7\images\musicplayer\slimshady_ready.png").convert_alpha(),
        pygame.image.load("D:/PP2python/lab7/images/musicplayer/natasha_ready.png").convert_alpha(),
        pygame.image.load("D:\PP2python\lab7\images\musicplayer\chase_ready.png").convert_alpha(),
        pygame.image.load("D:/PP2python/lab7/images/musicplayer/theweeknd_ready.png").convert_alpha(),
        pygame.image.load("D:\PP2python\lab7\images\musicplayer\darkhan_ready.png").convert_alpha(),
        pygame.image.load("D:\PP2python\lab7\images\musicplayer\ed_sheeran_ready.png").convert_alpha()
    ]
    
    #about sounds
    songs_list = [
        pygame.mixer.Sound("D:\PP2python\lab7\songs\The Neighbourhood - Sweater Weather.mp3"), 
        pygame.mixer.Sound("D:\PP2python\lab7\songs\Eminem — The Real Slim Shady.mp3"),
        pygame.mixer.Sound("D:\PP2python\lab7\songs\Eminem - Lose Your self.mp3"), 
        pygame.mixer.Sound("D:\PP2python\lab7\songs\Chase Atlantic - Heaven and back.mp3"),
        pygame.mixer.Sound("D:\PP2python\lab7\songs\The Weeknd feat. Gesaffelstein - I Was Never There.mp3"), 
        pygame.mixer.Sound("D:\PP2python\lab7\songs\darkhan-juzz-ude_(muzzona.kz).mp3"),
        pygame.mixer.Sound("D:\PP2python\lab7\songs\ed-sheeran-perfect.mp3")
    ]
    x = 1
    song_is_play = False
    #использую для пробела, остановить при первом и если еще раз начать песню
    stop_sound = True
    while True:
        #для позиции мышки
        mouse = pygame.mouse.get_pos()
        #стартовый экран
        if not song_is_play:
            screen.blit(bg, (0, 0))
        else:
            screen.blit(song_image_list[song_counter], (0, 0))

        # screen.blit(text, (50, 0))#
        # screen.blit(text, (50, 100))
        # screen.blit(text, (50, 200))
        # screen.blit(text, (50, 300))
        # screen.blit(text, (50, 400))
        # screen.blit(text, (50, 500))
        # screen.blit(text, (50, 600))
        
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            #обработка мышки
            if event.type == pygame.MOUSEBUTTONDOWN:
                for buttom in buttom_list:
                    if buttom.collidepoint(mouse) and not song_is_play:
                        song_counter = buttom_list.index(buttom)
                        songs_list[song_counter].play()
                        song_is_play = True

            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    song_is_play = False
                    songs_list[song_counter].stop()
                #старт секрет кнопка
                if event.key == pygame.K_q:
                    song_is_play = True
                    songs_list[song_counter].play()
                #смена песен вперед
                if event.key == pygame.K_d:
                    songs_list[song_counter].stop()
                    song_counter += 1
                    
                    #счетчик песен обработка
                    song_counter %= amount_of_songs
                    
                    songs_list[song_counter].play()
                #смена песен назад
                if event.key == pygame.K_a:
                    songs_list[song_counter].stop()
                    
                    if song_counter == 0:
                        song_counter = 6
                    else:
                        song_counter -= 1
                    #тоже чтобы не вышла за грань 
                    song_counter %= amount_of_songs
                    
                    songs_list[song_counter].play()
                #остановить или начать песню 
                if event.key == pygame.K_SPACE:
                    if stop_sound:
                        songs_list[song_counter].stop()
                        stop_sound = False
                    else:
                        songs_list[song_counter].play()
                        stop_sound = True
                
                    
                    
 
                
main()