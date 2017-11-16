import sys
import random
import pygame
from pygame.locals import *
import time
from itertools import cycle

from game import Game
from ship import Ship
from point import Point
from flying_stones import Stones
from star import Star
from bullet import Bullet
from shieldtoship import Shield
from enemyship import Enemyship
from enemybullet import Enemybullet



class Asteroids( Game ):
    def __init__(self, name, width, height):

        super().__init__( name, width, height )

        self.ship = Ship()

        self.asteroids = []
        for i in range(6):
            self.asteroids.append(Stones())
        
        self.stars=[]
        for i in range(30):
            self.stars.append(Star())
        
        self.bullets = []

        self.enemybullets = []


        self.shield = []


        self.enemyship = Enemyship()

        self.enemyship = None




        self.myfont = pygame.font.SysFont("monospace", 20, True)

        self.life = 3
        self.score = 0
        self.last = pygame.time.get_ticks()
        self.cooldown = 150
        self.spawnenemyship = 0





    def handle_input(self):
        super().handle_input()
        keys_pressed = pygame.key.get_pressed()
        self.spawnenemyship = random.randint(1, 400)
        print(self.spawnenemyship)
        if self.spawnenemyship == 200:
            self.enemyship = Enemyship()




        self.restart = keys_pressed[K_r]

        if (keys_pressed[K_LEFT] or keys_pressed[K_a]) and self.ship:
            self.ship.rotate(-5)

        if (keys_pressed[K_RIGHT] or keys_pressed[K_d]) and self.ship:
            self.ship.rotate(5)

        if (keys_pressed[K_UP] or keys_pressed[K_w]) and self.ship:
            self.ship.accelerate(0.5)

        if (keys_pressed[K_DOWN] or keys_pressed[K_s]) and self.ship:
            self.ship.accelerate(0)

        if keys_pressed[K_SPACE] and self.ship:
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.last = now
                if len(self.bullets) <= 10:
                    self.last = now
                    self.blastSound.play()
                    self.bullets.append(Bullet(self.ship.get_x(), self.ship.get_y(), self.ship.get_rotation()))


        if (keys_pressed[K_t]) and self.ship:
            now = pygame.time.get_ticks()
            print(now)
            if now - self.last >= 2000:
                self.ship.teleportShip()
                self.last = now

        if keys_pressed[K_s] and self.ship:

                self.shield.append(Shield(self.ship.get_x(), self.ship.get_y(), self.ship.get_rotation()))

        if keys_pressed[K_b] and self.ship:
            if len(self.enemybullets)==0 or self.enemybullets[-1].age() > 2000:
                self.enemybullets.append(Enemybullet(self.enemyship.get_x(), self.enemyship.get_y(), self.enemyship.get_rotation()))



    def update_simulation(self):

        super().update_simulation()

        if self.enemyship and self.ship:
             self.enemyship.update(self.width, self.height)
             self.enemyship.rotation = Point(self.enemyship.get_x(),self.enemyship.get_y()).getAngleBetwen( self.ship.position)

        if self.ship:
            self.ship.update( self.width, self.height )

        if self.forth == 2:
            for asteroid in self.asteroids:
                asteroid.update( self.width, self.height )
                if len(self.asteroids) < 6:
                    self.asteroids.append(Stones(asteroid.newStoneX(), asteroid.newStoneY()))
            self.forth = 0

        for bullet in self.bullets:
            if bullet.update(self.width, self.height) == True:
                    self.bullets.remove(bullet)

        for bullet in self.enemybullets:
            if bullet.update(self.width, self.height) == True:
                    self.enemybullets.remove(bullet)

        self.handle_collisions()

        self.asteroid_collision()

        self.bulletColideWithEnemyShip()

        self.enemyBulletCollideWithShip()
        #Asteroid-collision, utan = snabbare, med mycket coolare
        if self.ship:
            self.shieldCollision()

        for shield in self.shield:
            shield.update(self.ship.get_x(), self.ship.get_y() )


    def render_objects(self):
        super().render_objects()

        if self.ship:
            self.ship.draw( self.screen )

        for star in self.stars:
            star.draw( self.screen )

        for asteroid in self.asteroids:
            asteroid.draw( self.screen )

        for bullet in self.bullets:
            bullet.draw( self.screen )

        for shield in self.shield:
            shield.draw(self.screen)

        for enemybullet in self.enemybullets:
            enemybullet.draw(self.screen)

        if self.enemyship:
            self.enemyship.draw(self.screen)


        score = self.myfont.render("Score: {}".format(str(self.score)), 1, (255, 0, 0))
        self.screen.blit(score, (500, 5)) #500 i lådan, 650 utanför i fall att vi vill ha någonting annat där




        visible_life = self.life
        if visible_life < 0: visible_life = 0
        life = self.myfont.render("Life: {}".format(str(visible_life)), 1, (255, 0, 0))
        self.screen.blit(life, (70, 5))
        if (self.life < 0):
            self.gameOver()

        TpKnapp = self.myfont.render("t-For teleport", 1, (255, 255, 0))
        self.screen.blit(TpKnapp, (600, 520))

        Shieldknapp = self.myfont.render("S-For shield", 1, (255, 255, 0))
        self.screen.blit(Shieldknapp, (600, 540))



    def handle_collisions(self):

        if not self.ship:
            return

        for asteriod in self.asteroids:
            if asteriod.collide(self.ship):

                self.asteroids.remove(asteriod)
                self.life = self.life - 1
                        #Vänta tills nästa hit, så att man inte kan förlora alla liv på en gång

            for bullet in self.bullets:
                if asteriod.contains(bullet.position):
                    if asteriod.name == "L":
                        self.asteroids.remove(asteriod)
                        self.asteroids.append(Stones((asteriod.position.x -20), (asteriod.position.y + 20), "M"))
                        self.asteroids.append(Stones((asteriod.position.x + 20), (asteriod.position.y - 20), "M"))


                    elif asteriod.name == "M":
                        self.asteroids.remove(asteriod)
                    self.bullets.remove(bullet)
                    self.score += 10


    def asteroid_collision(self):
        #Asteroid-collision, endast stenar! :D
        for i in range(len(self.asteroids)):
            for j in range(len(self.asteroids)):
                if self.asteroids[i] != self.asteroids[j] and self.asteroids[i].distanceBetweenPosition(self.asteroids[j]) < 60:
                    if self.asteroids[i].collide(self.asteroids[j]):
                        self.asteroids[j].invertPull()
                        self.asteroids[i].invertPull()

    def shieldCollision(self):

        for asteroid in self.asteroids:
            if asteroid.collide(self.ship):
                self.asteroids.remove(asteroid)
            for shield in self.shield:
                if shield.shielddetection(asteroid):
                    self.shield.remove(shield)

    def enemyBulletCollideWithShip(self):
        for bullet in self.enemybullets:
            if self.ship.contains(bullet.position):
                self.enemybullets.remove(bullet)
                self.life = self.life -1


    def bulletColideWithEnemyShip(self):
        if not self.enemyship:
            return
        for bullet in self.bullets:
            if self.enemyship.contains(bullet.position):
                print("Boom Enemyship Dead")
                self.bullets.remove(bullet)
                self.enemyship = None












    def gameOver(self):
        #Game over skärmen!



        Game_Over = self.myfont.render("Game Over", 1, (255, 0, 0))
        onRestart = self.myfont.render("Press [R] to restart!", 2, (255, 255, 255))
        offRestart = self.myfont.render("Press [R] to restart!", 2, (150, 150, 150))
        self.screen.blit(Game_Over, (350, 250))

        self.screen.blit(onRestart, (280, 290))
        self.ship = None

            
        
            
