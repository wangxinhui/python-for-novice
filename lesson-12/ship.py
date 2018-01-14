import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False
        self.center = float(self.rect.centerx)
        self.ai_settings = ai_settings

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed
        self.rect.centerx = self.center

