import sys
import pygame
from gyro import Steel

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption('blue shy')
    # Создать изображение
    Ball = Steel(screen)#***
    bg_color = (255,255,255)# Установить цвет фона лазурно-синий

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:# Обнаружение игрока при нажатии кнопки закрытия игрового окна
                sys.exit()# выйти из игры
        # Перерисовывайте экран каждый раз при зацикливании
        screen.fill(bg_color)
        Ball.blitme() #***
        # Сделать видимым недавно нарисованный экран
        pygame.display.flip()

run_game()
