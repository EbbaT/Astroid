from polygon import *
from random import *
from random import randrange
import random
class Enemyship(Polygon):


    """Player Ship"""

    def __init__(self):

        self.ship_image = pygame.image.load("test_fighter.png")


        super().__init__([ Point(0 ,0), Point(-10 ,10), Point(15 ,0), Point(-10 ,-10) ], 0, 100, 0)


        """
        Checking checking
        """


        #self.pull = Point(0.5, 0.5)
        #self.angular_velocity = 0.1
       # self.rotation = random.randrange(0, 359, 15)

        self.rotation = random.randrange(0, 359, 15)
        # Hur snabbt asteroiden roterar

        self.pull = Point(round(random.uniform(-1, 1), 1), round(random.uniform(-1, 1), 1))
        # Vilken hastighet den åker i

        self.angular_velocity = round(random.uniform(-1, 1), 1)
        # Hur mycket den ska rotera i varje steg

    def followShip(self, newx, newy):
        self.Point = Point(newx,newy)







    def draw(self, screen):
        scaled_image  = pygame.transform.scale( self.ship_image, (50 ,50) )
        rotated_image = pygame.transform.rotate( scaled_image, -self.rotation)
        x = self.position.x #-rotated_image.get_width( ) /2
        y = self.position.y #-rotated_image.get_height() / 2
        screen.blit(rotated_image, (x, y))

    def teleportShip(self):
        self.position.x = randint(1, 640)
        self.position.y = randint(1, 480)

