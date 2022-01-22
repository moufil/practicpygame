import pygame

class Steel():
    def __init__(self, screen):
        self.screen = screen



        self.image = pygame.image.load("E:\Python\Games zadaci\op.bmp")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.centery = self.screen_rect.centery

    def blitme(self):
        '' 'Нарисуйте изображение в указанном месте' ''
        self.screen.blit(self.image, self.image_rect,)
