from polygon import Polygon
from point import Point
import os, pygame
from circle import Circle
from shape import Shape
from random import randint
class Ship(Polygon):

    """Player Ship"""

    def __init__(self):

        self.ship_image = pygame.image.load("test_fighter.png")
        

        super().__init__([ Point(0,0), Point(-10,10), Point(15,0), Point(-10,-10) ], 320, 240, 0)


        """
        Checking checking
        """

        self.pull = Point(0, -0.1)
        self.angular_velocity = 0.0


    def get_x(self):
        return self.position.getX()

    def get_y(self):
        return self.position.getY()

    def get_rotation(self):
        return self.rotation

    def draw(self, screen):
        scaled_image  = pygame.transform.scale( self.ship_image, (50,50) )
        rotated_image = pygame.transform.rotate( scaled_image, -self.rotation)
        x = self.position.x-rotated_image.get_width()/2
        y = self.position.y -rotated_image.get_height()/2
        screen.blit(rotated_image, (x, y))

    def teleportShip(self):
        self.position.x = randint(1,640)
        self.position.y = randint(1,480)



        





