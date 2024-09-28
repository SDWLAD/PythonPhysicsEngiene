from physicsObject import PhysicsObject
import pygame as pg

class CircleObject(PhysicsObject):
    def __init__(self, position, radius):
        super().__init__()
        self.position = position
        self.radius = radius
        self.weight = 0.5

    def draw(self, sc):
        pg.draw.circle(sc, (255, 255, 255), self.position, self.radius)