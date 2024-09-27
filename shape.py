from pygame import Vector2
import pygame as pg

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = Vector2(5, -5)
        self.weight = 0.1
        self.drag = 0.99
    
    def draw(self, sc):
        pg.draw.circle(sc, (255, 255, 255), (self.x, self.y), 5)
    
    def gravity(self):
        self.velocity.y += self.weight

    def update(self):
        self.velocity *= self.drag
        self.gravity()
        self.x += self.velocity.x
        self.y += self.velocity.y