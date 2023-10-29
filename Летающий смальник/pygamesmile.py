from msilib import Control
import pygame as pg
import sys, controls
from igrok import Smile


#настройки окна
def run():
#рашерение экрана
  W = 340
  H  = 240
  
  
  pg.init()

  screen = pg.display.set_mode((W,H))
  pg.display.set_caption('Смальня :)')
  pg.display.set_icon(pg.image.load('images/icon.png'))
  backround = pg.image.load('images/backround.jpg')
  backround = pg.transform.scale(backround, (W, H))
  bg_color = (255, 182, 193)
  #вызывает класс смайльника
  smile = Smile(screen)
  
  while True:
    controls.event(smile)

    #закрашивает фон
    screen.blit(backround, (0,0))
    #рисует сам смальник на экран
    smile.output()
    pg.display.flip()
    

run()