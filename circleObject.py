# import math
# from boxObject import BoxObject
from physicsObject import PhysicsObject
import pygame as pg
from settings import SCREEN_SIZE
from pygame import Vector2

class CircleObject(PhysicsObject):
    def __init__(self, position, radius):
        super().__init__()
        self.position = position
        self.radius = radius/2
        self.mass = 0.5
    
    def is_collision(self, other):
        if isinstance(other, CircleObject):
            if (self.position - other.position).length() < self.radius + other.radius:
                return True
        # if isinstance(other, BoxObject):
        #     dx = self.position.x - other.rect.centerx
        #     dy = self.position.y - other.rect.centery
        #     distance = math.hypot(dx, dy)
        #     if distance < self.radius + other.rect.width/2:
        #         return True
        return False
    
    def check_collisions(self, other):
        if self.is_collision(other):            
            dis = self.position - other.position
            dif = self.radius+other.radius-dis.length()

            try:dis = dis.normalize()
            except:...

            ave_elasticity = ((self.elasticity+other.elasticity)/2)
            d1 = dis * (dif/2)
            d2 = dis * dif * ave_elasticity * 10

            self.position += d1
            other.position += -d1
            self.velocity += d2
            other.velocity += -d2

    def clamp_display(self):
        if self.position.x - self.radius < 0:
            self.position = Vector2(self.radius, self.position.y)
            self.velocity = Vector2(abs(self.velocity.x)*self.elasticity, self.velocity.y)

        if self.position.x + self.radius > SCREEN_SIZE[0]:
            self.position = Vector2(SCREEN_SIZE[0]-self.radius, self.position.y)
            self.velocity = Vector2(-abs(self.velocity.x)*self.elasticity, self.velocity.y)

        if self.position.y - self.radius < 0:
            self.position = Vector2(self.position.x, self.radius)
            self.velocity = Vector2(self.velocity.x, abs(self.velocity.y)*self.elasticity)

        if self.position.y + self.radius > SCREEN_SIZE[1]:
            self.position = Vector2(self.position.x, SCREEN_SIZE[1]-self.radius)
            self.velocity = Vector2(self.velocity.x, -abs(self.velocity.y)*self.elasticity)

    def draw(self, sc):
        pg.draw.circle(sc, self.color, self.position, self.radius)