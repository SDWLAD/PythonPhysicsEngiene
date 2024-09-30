from physicsObject import PhysicsObject
import pygame as pg

class CircleObject(PhysicsObject):
    def __init__(self, position, radius):
        super().__init__()
        self.position = position
        self.radius = radius
        self.mass = 0.5
    
    def is_collision(self, other):
        if isinstance(other, CircleObject):
            if (self.position - other.position).length() < self.radius + other.radius:
                return True
        return False

    def draw(self, sc):
        pg.draw.circle(sc, (255, 255, 255), self.position, self.radius)