from random import randint
import pygame as pg
from circleObject import CircleObject
from physicsObject import PhysicsObject
from settings import *

sc = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

objects = [
    CircleObject(pg.Vector2(410, 350), 10),
    CircleObject(pg.Vector2(400, 400), 10),
]


while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            quit()
    sc.fill((0, 0, 0))

    if pg.mouse.get_pressed()[0]:
        pos = pg.mouse.get_pos()
        r = 20
        rotation = pg.Vector2(randint(-100, 100)/100, randint(-100, 100)/100).normalize()*r
        objects.append(CircleObject(pg.Vector2(pos[0], pos[1])+rotation, 10))

    for obj in objects:
        obj.update()
        obj.draw(sc)

        
    pg.display.flip()
    clock.tick(40)