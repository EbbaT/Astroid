from ship import *

class Enemyship(Ship):
   

    def __init__(self):
        ship_image = pygame.image.load("Tank_SU.png")
        # self.ship_image = pygame.image.load("falcon2.png")
        # Min not so good Falcon ;_;
        ship_image = pygame.transform.scale(ship_image, (50, 50))

        self.points = [Point(-17, -20), Point(10, -20), Point(25, -2), Point(0, 20), Point(-20, 15), Point(-25, 0)]

        super().__init__(ship_image)
        self.position.x = 10
        self.position.y = 300
        self.rotation = 2

        self.pull = Point(0, -0.1)
        # En liten pull uppåt när man startar spelet

        self.angular_velocity = 1

    def getE_x(self):
        return self.position.getX()

    def getE_y(self):
        return self.position.getY()

    def getE_rotation(self):
        return self.rotation






