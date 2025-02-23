from random import randint
import pygame as pg
from circleObject import CircleObject
from boxObject import BoxObject
from physicsObject import PhysicsObject
from settings import *
import settings
import math

sc = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

objects = []

n, r = 50, 500
# objects = [CircleObject(pg.Vector2(((r/n)*i) * math.cos(2 * math.pi * i / n) + SCREEN_SIZE[0]/2, ((r/n)*i) * math.sin(2 * math.pi * i / n) + SCREEN_SIZE[1]/2), 10) for i in range(n)]
# objects = [BoxObject(pg.Vector2(((r/n)*i) * math.cos(2 * math.pi * i / n) + SCREEN_SIZE[0]/2, ((r/n)*i) * math.sin(2 * math.pi * i / n) + SCREEN_SIZE[1]/2), 10) for i in range(n)]

obj_type = 0

while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            quit()
        if e.type == pg.MOUSEWHEEL:
            new_ball_size+=e.y
            new_ball_size = min(max(1, new_ball_size), 50)
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_SPACE:
                obj_type += 1
                obj_type = obj_type % 2
    sc.fill((0, 0, 0))

    if pg.mouse.get_pressed()[0]:
        pos = pg.mouse.get_pos()
        r = 20
        rotation = pg.Vector2(randint(-100, 100)/100, randint(-100, 100)/100).normalize()*r

        objects.append([
            CircleObject(pg.Vector2(pos[0], pos[1])+rotation, new_ball_size),
            BoxObject(rect=pg.Rect(pos[0], pos[1], new_ball_size, new_ball_size))
        ][obj_type])


    if pg.mouse.get_pressed()[2]:
        x, y = pg.mouse.get_pos()
        settings.gravity_point.x = x
        settings.gravity_point.y = y

    for obj in objects:
        obj.update()
        obj.draw(sc)
    
    sc.blit(pg.font.SysFont('Arial', 20).render(str(new_ball_size), False, (255, 255, 255)), (0, 0))
    sc.blit(pg.font.SysFont('Arial', 20).render(f"FPS: {str(round(clock.get_fps()))}", False, (255, 255, 255)), (0, 20))
    sc.blit(pg.font.SysFont('Arial', 20).render(f"Count: {str(len(objects))}", False, (255, 255, 255)), (0, 40))

    pg.display.flip()
    clock.tick(40)