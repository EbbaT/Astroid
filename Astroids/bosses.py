from shape import Shape
from polygon import Polygon
from point import Point
import random, os, pygame
from circle import Circle


class Bosses(Polygon):
    def __init__(self,bosslife= 20):#extragrejjertillbossen
        self.life = bosslife
        super().__init__( points=[], x=320,y=240,rotation=5)
        self.points = [Point(0,0), Point(66,60), Point(66, 120), Point(-33, 33)]
        #self.x = 200
        #self.y = 400
        self.rotation = 2
        superboss= []
        self.rotation = random.randrange(0, 359, 15)
        # Hur snabbt asteroiden roterar

        self.pull = Point(round(random.uniform(-1, 1), 1), round(random.uniform(-1, 1), 1))
        # Vilken hastighet den åker i

        self.angular_velocity = round(random.uniform(-1, 1), 1)








