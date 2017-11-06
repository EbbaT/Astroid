from circle import Circle
from point import Point
import random



class Star(Circle):
    """Stars!!"""
    def __init__(self):
        self.radius = 1
        self.linewidth = 1
        self.color = (255,255,255)


        self.position = Point(random.randrange(0, 640, 5), random.randrange(0, 480, 5))
        #Startposition

        self.rotation = 0
        #Hur snabbt stjärnan roterar

        self.pull = Point(0, 0)
        #Vilken hastighet den åker i

        self.angular_velocity = 0
        #Hur många grader den snurrar per steg

