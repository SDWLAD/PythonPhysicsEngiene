from pygame import Vector2
import pygame as pg

class PhysicsObject:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(10, 0)
        self.weight = 1
        self.drag = 1
    
    def draw(self, sc):...
    
    def gravity(self):
        self.velocity.y += self.weight

    def update(self):
        self.velocity *= self.drag
        self.gravity()
        self.position += self.velocity