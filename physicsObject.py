from pygame import Vector2
import pygame as pg

class PhysicsObject:

    _all_objects = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls._all_objects.append(instance)
        return instance

    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.mass = 1
        self.drag = 1
        self.kinematic = False
    
    def draw(self, sc):...
    
    def gravity(self):
        gravity = Vector2(0, 0.098*self.mass)
        self.acceleration += gravity
    
    def is_collision(self, other):...

    def update(self):
        if self.kinematic: return
        self.gravity()
        self.velocity += self.acceleration
        self.velocity *= self.drag
        self.position += self.velocity
    
    @classmethod
    def check_collisions(cls):
        for i in range(len(cls._all_objects)):
            for j in range(i + 1, len(cls._all_objects)):
                if cls._all_objects[i].is_collision(cls._all_objects[j]):
                    this_object:PhysicsObject = cls._all_objects[i]
                    other_object:PhysicsObject = cls._all_objects[j]
                    this_object.acceleration.y=1
                    this_object.velocity.y=-1