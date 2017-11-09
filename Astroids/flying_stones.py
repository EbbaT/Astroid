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

        self.name = "L"

        self.big = pygame.transform.scale(self.big, (60,60) )
        self.medium = pygame.transform.scale( self.medium, (40,40) )

        medium = [Point(0, 18), Point(-15, 5), Point(0, -13) , Point(20, -13), Point(20, 5) ]
        big = [Point(20, 20), Point(-15, 20), Point(-25, 10) ,Point(-10, -20) ,Point(20, -15), Point(30, 0)]

        self.picture = self.big

        if self.picture == self.big:
            self.points = big

            if bool == False:
                self.position = Point(random.randrange(0, 640, 5), random.randrange(0, 480, 5))
                #Startposition

            elif bool == True:
                self.newStone()


        elif self.picture == self.medium:
            self.points = medium

        
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

    def mediumStone(self, position):
        self.name = "M"
        self.picture = self.medium
        self.position = position


        


