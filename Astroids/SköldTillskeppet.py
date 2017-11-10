
from circle import  *
class Shield(Circle):
    """Shooting things like a bass"""

    def __init__(self, x, y, rot):
        super().__init__(x, y, 60, rot)

        self.linewidth = 1

        self.color = (255, 255, 0)

        self.rotation = rot

        self.accelerate(0)

        self.angular_velocity = 0

        self.position = Point(x, y)

    def update(self, width, height):
        self.position.x
        self.position.y

        self.position += self.pull
        self.rotation += self.angular_velocity

    def followShip(self, x, y):
        self.position = Point(x, y)





