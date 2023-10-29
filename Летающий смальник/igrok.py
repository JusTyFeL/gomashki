import pygame as pg

class Smile():
    #создание смайльника 
    def __init__(self,screen):
        self.screem = screen
        self.image = pg.image.load('images/igrok.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        #рисует сам смайлик
        self.screem.blit(self.image,self.rect)
        