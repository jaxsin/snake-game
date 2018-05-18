import pygame
pygame.init()
screen_width= 1000
screen_length=1000
gameScreen= pygame.display.set_mode((screen_width,screen_length))
white=(255,255,255)
def game_loop():
    game=True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameScreen.fill(white)
        pygame.display.update()
game_loop()

