import pygame as pg
pg.init()

new_ball_size = 10

SCREEN_SIZE = (1280, 720)
gravity_direction = pg.Vector2(0, 1)
gravity_point = None