from circle import Circle
from point import Point

class Bullet(Circle):
    """Shooting things like a bass"""

    def __init__(self, x, y, rot):

        super().__init__(x, y, 3, rot)

        self.linewidth = 0
        
        self.color = (255, 0, 0)

        self.rotation = rot
        
        self.accelerate(10)

        self.angular_velocity = 0

        self.position = Point(x, y)


    def update(self, width, height):

        self.position.x
        self.position.y


        self.position += self.pull
        self.rotation += self.angular_velocity

        
        
        if self.position.x < 0 or self.position.x > width or self.position.y < 0 or self.position.y > height:

            return True

        else:
            return False



