from random import randint
import pygame as pg
from circleObject import CircleObject
from physicsObject import PhysicsObject
from settings import *
import settings
import math

sc = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

objects = []

n, r = 50, 500
objects = [CircleObject(pg.Vector2(((r/n)*i) * math.cos(2 * math.pi * i / n) + SCREEN_SIZE[0]/2, ((r/n)*i) * math.sin(2 * math.pi * i / n) + SCREEN_SIZE[1]/2), 10) for i in range(n)]

while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            quit()
        if e.type == pg.MOUSEWHEEL:
            new_ball_size+=e.y
    sc.fill((0, 0, 0))

    if pg.mouse.get_pressed()[0]:
        pos = pg.mouse.get_pos()
        r = 20
        rotation = pg.Vector2(randint(-100, 100)/100, randint(-100, 100)/100).normalize()*r
        objects.append(CircleObject(pg.Vector2(pos[0], pos[1])+rotation, new_ball_size))
    if pg.mouse.get_pressed()[2]:
        x, y = pg.mouse.get_pos()
        settings.gravity_point.x = x
        settings.gravity_point.y = y

    for obj in objects:
        obj.update()
        obj.draw(sc)
             
    pg.display.flip()
    clock.tick(40)