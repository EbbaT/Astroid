import sys
import random
import pygame
from pygame.locals import *
import time

from game import Game
from ship import Ship
from point import Point
from flying_stones import *
from star import Star
from bullet import Bullet
from bosses import *


##

class Asteroids( Game ):
    """
    Asteroids extends the base class Game to provide logic for the specifics of the game
    """
    def __init__(self, name, width, height):
        super().__init__( name, width, height )

        self.ship = Ship()
        #  TODO: should create a Ship object here
        
        # TODO: should create asteroids
        self.asteroids = []
        for i in range(8):
            self.asteroids.append(Stones("False"))
        
        # TODO: should create stars
        self.stars=[]
        for i in range(100):
            self.stars.append(Star())


        
        self.bosses = []
        for i in range(1):
            self.bosses.append(Bosses())

        self.bullets = []

        self.myfont = pygame.font.SysFont("monospace", 20, True)

        self.life = 3
        self.score = 0
        self.last = pygame.time.get_ticks()
        self.cooldown = 150
        self.LargeAstroidCounter = 8
        self.tpcd = time.time()
        self.bosslife = 100





    def handle_input(self):
        super().handle_input()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT] and self.ship:
            self.ship.rotate(-3)
        if keys_pressed[K_RIGHT] and self.ship:
            self.ship.rotate(3)
        if keys_pressed[K_UP] and self.ship:
            self.ship.accelerate(0.05)
        if keys_pressed[K_DOWN] and self.ship:
            self.ship.accelerate(0)
        if keys_pressed[K_SPACE] and self.ship:
            # TODO: should create a bullet when the user fires
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.last = now
                if len(self.bullets) <= 10:
                    self.last = now
                    self.bullets.append(Bullet(self.ship.get_x(), self.ship.get_y(), self.ship.get_rotation()))

        if keys_pressed[K_t] and self.ship:
            now = pygame.time.get_ticks()
            print(now)
            if now - self.last >= 2000:

                self.ship.teleportShip()
                self.last = now

    def update_simulation(self):
        """
        update_simulation() causes all objects in the game to update themselves
        """
        super().update_simulation()

        if self.ship:
            self.ship.update( self.width, self.height )

        for asteroid in self.asteroids:
            asteroid.update( self.width, self.height )
            if len(self.asteroids) < self.LargeAstroidCounter:
                self.asteroids.append(Stones("True"))
            elif self.LargeAstroidCounter == 0:
                self.LargeAstroidCounter = 12

        for bosses in self.bosses:
            bosses.update(self.width, self.height)



        #for star in self.stars:
            #star.update( self.width, self.height )

        # TODO: should probably call update on our bullet/bullets here
        for bullet in self.bullets:
            if bullet.update(self.width, self.height) == True:
                    self.bullets.remove(bullet)


        # TODO: should probably work out how to remove a bullet when it gets old
        self.handle_collisions()

    def render_objects(self):
        """
        render_objects() causes all objects in the game to draw themselves onto the screen
        """
        super().render_objects()
        # Render the ship:

        if self.ship:
            self.ship.draw( self.screen )
        # Render all the stars, if any:

        for star in self.stars:
            star.draw( self.screen )
        # Render all the asteroids, if any:

        for asteroid in self.asteroids:
            asteroid.draw( self.screen )
        # Render all the bullet, if any:

        for bullet in self.bullets:
            bullet.draw( self.screen )


        for bosses in self.bosses:
            bosses.draw( self.screen)



        score = self.myfont.render("Score: {}".format(str(self.score)), 1, (255, 255, 0))
        self.screen.blit(score, (525,10))

        life = self.myfont.render("Life: {}".format(str(self.life)), 1, (255, 255, 0))
        self.screen.blit(life, (525, 30))

        bosslife = self.myfont.render("Bosslife: {}".format(str(self.bosslife)), 1, (0, 255, 0))
        self.screen.blit(bosslife, (450, 50))
        self.tpknapp = "T"
        tpknapp = self.myfont.render("Tpknapp: {}".format(str(self.tpknapp)), 1, (0, 255, 0))
        self.screen.blit(tpknapp, (10, 50))


    def handle_collisions(self):
        """
        handle_collisions() should check:
            - if our ship has crashed into an asteroid (the ship gets destroyed - game over!)
            - if a bullet has hit an asteroid (the asteroid gets destroyed)
        :return: 
        """
        # TODO: implement collission detection,
        #       using the collission detection methods in all of the shapes

        for asteriod in self.asteroids:
            if asteriod.contains(self.ship.position):
                    self.asteroids.remove(asteriod)
                    self.life = self.life - 1
                    self.ship.teleportshiintomidle()

            for bullet in self.bullets:
                if asteriod.contains(bullet.position):
                    if asteriod.astroidnamn == "M":
                        self.asteroids.remove(asteriod)
                        self.bullets.remove(bullet)
                    elif asteriod.astroidnamn == "L":
                        self.LargeAstroidCounter = self.LargeAstroidCounter - 1
                        print (self.LargeAstroidCounter)
                        self.asteroids.remove(asteriod)
                        self.asteroids.append(Stones("Medium",asteriod.position.x, asteriod.position.y))
                        self.asteroids.append(Stones("Medium", asteriod.position.x, asteriod.position.y))
                        self.bullets.remove(bullet)
                        self.score  = self.score + 1

        for boss in self.bosses:
            if boss.contains(self.ship.position):
                self.life = self.life - 1
            for bullets in self.bullets:
                if boss.contains(bullets.position):
                    self.bosslife = self.bosslife -1
                    self.bullets.remove(bullet)
                if self.bosslife == 0:
                    self.bosses.remove(boss)





