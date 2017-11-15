from polygon import Polygon
from point import Point
import os, pygame
from circle import Circle
from shape import Shape
from random import *

class Ship(Polygon):

    """Player Ship"""

    def __init__(self, ship_image=None):
        if not ship_image:
            self.ship_image = pygame.image.load("test_fighter.png")
        else:
            self.ship_image = ship_image
        #self.ship_image = pygame.image.load("falcon2.png")
        #Min not so good Falcon ;_;
        self.ship_image = pygame.transform.scale( self.ship_image, (50,50) )

        size = [Point(-17,-20), Point(10, -20), Point(25, -2), Point(0, 20),Point(-20, 15), Point(-25, 0) ]

        super().__init__(self.ship_image, size, 400, 300, 0)

        self.pull = Point(0, -0.1)
        #En liten pull uppåt när man startar spelet

        self.angular_velocity = 0.0


    def get_x(self):
        return self.position.getX()

    def get_y(self):
        return self.position.getY()

    def get_rotation(self):
        return self.rotation

    def teleportShip(self):
        self.position.x = randint(1, 640)
        self.position.y = randint(1, 480)



        





