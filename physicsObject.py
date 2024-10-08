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
        self.kinematic = False
        self.player = False
        self.elasticity = 0.03
    
    def draw(self, sc):...
    def clamp_display(self):...
    def is_collision(self, other):...
    
    def gravity(self):
        gravity = Vector2(0, 0.9807)
        self.velocity += gravity
    

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]: self.velocity.y = -1
        if keys[pg.K_DOWN]: self.velocity.y = 1
        if keys[pg.K_LEFT]: self.velocity.x = -1
        if keys[pg.K_RIGHT]: self.velocity.x = 1

    def update(self):
        if self.kinematic: return
        if self.player: self.control()

        self.gravity()
        self.position += self.velocity
        self.clamp_display()
    

    @classmethod
    def check_collisions(cls):
        for i in range(len(cls._all_objects)):
            for j in range(len(cls._all_objects)):
                if cls._all_objects[i].is_collision(cls._all_objects[j]):
                    this_object:PhysicsObject = cls._all_objects[i]
                    other_object:PhysicsObject = cls._all_objects[j]
                    
                    dis = this_object.position - other_object.position
                    dif = this_object.radius+other_object.radius-dis.length()

                    try:dis = dis.normalize()
                    except:...

                    ave_elasticity = ((this_object.elasticity+other_object.elasticity)/2)
                    d1 = dis * (dif/2)
                    d2 = dis * dif * ave_elasticity * 10

                    this_object.position += d1
                    other_object.position += -d1
                    this_object.velocity += d2
                    other_object.velocity += -d2