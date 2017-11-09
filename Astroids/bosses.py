from shape import Shape
from polygon import Polygon
from point import Point
import random, os, pygame
from circle import Circle
class Bosses(Polygon):
    def __init__(self):
        super().__init__()

        Bossen = [Point(10, 3), Point(22, 11), Point(12, 10), Point(0, 0)]