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

        #big_asteroid = [Point(10,30), Point(25,25), Point(33,11), Point(35,-7), Point(21,-13), Point(13,-29), Point(-13,-31), Point(-21,-28), Point(-28,-22), Point(-34,-6), Point(-32,14), Point(-29, 21), Point(-15, 9), Point(-23, 24), Point(-10, 30)]
        
        #medium_asteroid = [Point(-12, 12), Point(-13, 17), Point(15, 19), Point(20, 12), Point(17, -5), Point(14, -10), Point(-2, -13), Point(-12, -5), Point(-10, 2), Point(-9, 5)]
        
        #small_asteroid = [Point(10,3), Point(22,11), Point(12, 10), Point(0, 0)]

        self.scaled_image = random.choice([self.big, self.medium])

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


    def draw(self, screen):

        #scaled_image  = pygame.transform.scale( self.big, (40,40) )

        rotated_image = pygame.transform.rotate(scaled_image, self.rotation)

        x = self.position.x - rotated_image.get_width()/2

        y = self.position.y -  rotated_image.get_height()/2

        screen.blit(rotated_image, (x, y))


        


        


