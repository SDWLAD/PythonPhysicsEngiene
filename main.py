from pygame import *

sc = display.set_mode((800, 600))
clock = time.Clock()

while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()
    sc.fill((0, 0, 0))
    display.flip()
    clock.tick(60)