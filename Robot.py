from rrb2 import *
import pygame
from pygame.locals import *
from time import sleep
rr = RRB2()

pygame.init()

screen = pygame.display.set_mode((0, 0))


while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print "test1"
            if event.key == K_UP:
                print "test"
                rr.forward(1)
                rr.set_led1(True)
                rr.set_led2(True)
            elif event.key == K_DOWN:
                rr.set_led1(True)
                rr.set_led2(True)
                rr.reverse(1)
            elif event.key == K_LEFT:
                rr.set_led1(False)
                rr.set_led2(True)
                rr.set_motors(1,1,1,0)
                sleep(1)
                rr.stop()
            elif event.key == K_RIGHT:
                rr.set_led1(True)
                rr.set_led2(False)
                rr.set_motors(1,0,1,1)
                sleep(1)
                rr.stop()
            elif event.key == K_SPACE:
                rr.stop()
                rr.set_led1(False)
                rr.set_led2(False)
        else: rr.stop
                rr.set_led2(False)
        else: rr.stop