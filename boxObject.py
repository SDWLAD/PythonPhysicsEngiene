import math
from circleObject import CircleObject
from physicsObject import PhysicsObject
import pygame as pg
from settings import SCREEN_SIZE
from pygame import Vector2

class BoxObject(PhysicsObject):
    def __init__(self, rect):
        super().__init__()
        self.rect = rect
        self.position = self.rect.center
        self.mass = 0.5
    
    def is_collision(self, other):
        if isinstance(other, BoxObject):
            if self.rect.colliderect(other.rect):
                return True
        if isinstance(other, CircleObject):
            dx = self.rect.centerx - other.position.x
            dy = self.rect.centery - other.position.y
            distance = math.hypot(dx, dy)
            if distance < self.rect.width/2 + other.radius:
                return True
        return False
    
    def check_collisions(self, other):
        self.rect.center = self.position
        if not "rect" in other.__dict__: other.rect = pg.Rect(*other.position, other.radius*2, other.radius*2)
        if self.is_collision(other):
            dis = Vector2(self.rect.center) - Vector2(other.rect.center)
            overlap_x = (self.rect.width / 2 + other.rect.width / 2) - abs(dis.x)
            overlap_y = (self.rect.height / 2 + other.rect.height / 2) - abs(dis.y)

            if overlap_x > 0 and overlap_y > 0:
                if overlap_x < overlap_y:
                    if dis.x > 0:
                        self.rect.x += overlap_x / 2
                        other.rect.x -= overlap_x / 2
                    else:
                        self.rect.x -= overlap_x / 2
                        other.rect.x += overlap_x / 2
                else:
                    if dis.y > 0:
                        self.rect.y += overlap_y / 2
                        other.rect.y -= overlap_y / 2
                    else:
                        self.rect.y -= overlap_y / 2
                        other.rect.y += overlap_y / 2
        self.position = self.rect.center

    def clamp_display(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x = abs(self.velocity.x) * self.elasticity

        if self.rect.right > SCREEN_SIZE[0]:
            self.rect.right = SCREEN_SIZE[0]
            self.velocity.x = -abs(self.velocity.x) * self.elasticity

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y = abs(self.velocity.y) * self.elasticity

        if self.rect.bottom > SCREEN_SIZE[1]:
            self.rect.bottom = SCREEN_SIZE[1]
            self.position.y = self.rect.centery
            self.velocity.y = -abs(self.velocity.y) * self.elasticity

    def draw(self, sc):
        pg.draw.rect(sc, self.color, self.rect)