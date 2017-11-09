from shape import Shape
from polygon import Polygon
from point import Point
import random, os, pygame
from circle import Circle


class Stones(Polygon):

    """Asteroidsssss"""

    def __init__(self, bool):
        
        self.big = pygame.image.load("asteroid_test_stone1.png")
        self.medium = pygame.image.load("asteroid_test_stone2.png")


        self.big = pygame.transform.scale(self.big, (60,60) )
        self.medium = pygame.transform.scale( self.medium, (40,40) )

        medium = [Point(10,10), Point(-10, -10), Point(5,5) ]
        big = [Point(15,15), Point(-15, -15), Point(10,10) ]

        self.picture = random.choice([self.big, self.medium])

        if self.picture == self.big:
            self.points = big
        elif self.picture == self.medium:
            self.points = medium



        if bool == False:
            self.position = Point(random.randrange(0, 640, 5), random.randrange(0, 480, 5))
            #Startposition
        elif bool == True:
            self.newStone()


        self.rotation = random.randrange(0, 359, 15)
        #Hur snabbt asteroiden roterar

        self.pull = Point(round(random.uniform(-1, 1), 1), round(random.uniform(-1, 1), 1))
        #Vilken hastighet den åker i

        self.angular_velocity = round(random.uniform(-1, 1), 1)
        #Hur mycket den ska rotera i varje steg


    def newStone(self):

        posx = Point(random.randrange(0, 640, 5), 0)
        posy = Point(0, random.randrange(0, 480, 5))
        self.position = random.choice([posx, posy])

        return self.position


        


        


