from ship import *

class Enemyship(Ship):
   

    def __init__(self):
        ship_image = pygame.image.load("Tank_SU.png")
        # self.ship_image = pygame.image.load("falcon2.png")
        # Min not so good Falcon ;_;
        ship_image = pygame.transform.scale(ship_image, (50, 50))

        self.points = [Point(-17, -20), Point(10, -20), Point(25, -2), Point(0, 20), Point(-20, 15), Point(-25, 0)]

        super().__init__(ship_image)
        self.position.x = randint(1,640)
        self.position.y = randint(1,480)
        self.rotation = 2

        self.pull = Point(1, -1)
        # En liten pull uppåt när man startar spelet

        self.angular_velocity = 1






