import sys 
import pygame as pg
pg.init()

win_x,win_y = 800,480
screen = pg.display.set_mode((win_x, win_y))
press_w = False
press_a = False
press_s = False
press_d = False
w = 0
a = 0
s = 0
d = 0
posX , posY = 400,240
while(True):
    screen.fill((255,255,255))
    pg.draw.rect(screen,(255,255,0),(posX -a +d,posY -w +s ,100,100))

    pg.display.update()
    pg.time.delay(3)
    
    if press_w:
        w += 1
    if press_a:
        a += 1
    if press_s:
        s += 1
    if press_d:
        d += 1

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_w :
            press_w = True
        if event.type == pg.KEYUP and event.key == pg.K_w :
            press_w = False
            
        if event.type == pg.KEYDOWN and event.key == pg.K_a :
            press_a = True
        if event.type == pg.KEYUP and event.key == pg.K_a :
            press_a = False
            
        if event.type == pg.KEYDOWN and event.key == pg.K_s :
            press_s = True
        if event.type == pg.KEYUP and event.key == pg.K_s :
            press_s = False
            
        if event.type == pg.KEYDOWN and event.key == pg.K_d :
            press_d = True
        if event.type == pg.KEYUP and event.key == pg.K_d :
            press_d = False
            
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        