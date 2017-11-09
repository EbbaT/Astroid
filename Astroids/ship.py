from polygon import Polygon
from point import Point
import os, pygame
from circle import Circle
from shape import Shape

class Ship(Polygon):

    """Player Ship"""

    def __init__(self):

        self.ship_image = pygame.image.load("falcon2.png")
        self.ship_image = pygame.transform.scale( self.ship_image, (50,50) )

        size = [Point(0,0), Point(-10,10), Point(-10,-10), Point(15, 0)]

        super().__init__(self.ship_image, size, 320, 240, 0)

        self.pull = Point(0, -0.1)
        self.angular_velocity = 0.0


    def get_x(self):
        return self.position.getX()

    def get_y(self):
        return self.position.getY()

    def get_rotation(self):
        return self.rotation



        





