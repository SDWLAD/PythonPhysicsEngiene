import pygame as pg
from circleObject import CircleObject

sc = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

objects = [
    CircleObject(pg.Vector2(400, 300), 10),
    CircleObject(pg.Vector2(400, 400), 10),
]

while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            quit()
    sc.fill((0, 0, 0))

    for obj in objects:
        obj.update()
        obj.draw(sc)

    pg.display.flip()
    clock.tick(60)