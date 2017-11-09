from shape import Shape
from polygon import Polygon
from point import Point
import random, os, pygame
from circle import Circle


class Bosses(Polygon):
    def __init__(self, life):  #extragrejjertillbossen
        if superboss:
            x=200
            y=400
            rotation=2
        else:
            x=100
            y=300
            rotation=4
        super().__init__( points=[], x, 500, rotation)
        self.points = [Point(-12, 12), Point(-13, 17), Point(15, 19), Point(20, 12), Point(17, -5), Point(14, -10), Point(-2, -13), Point(-12, -5)]
        #self.x = 200
        #self.y = 400
        self.rotation = 2
        superboss= []








