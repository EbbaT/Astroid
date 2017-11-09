import sys
import random
import pygame
from pygame.locals import *
import time

from game import Game
from ship import Ship
from point import Point
from flying_stones import Stones
from star import Star
from bullet import Bullet


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
            self.asteroids.append(Stones(False))
        
        # TODO: should create stars
        self.stars=[]
        for i in range(100):
            self.stars.append(Star())
        

        self.bullets = []


    def handle_input(self):
        super().handle_input()
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[K_LEFT] or keys_pressed[K_a]) and self.ship:
            self.ship.rotate(-3)
        if (keys_pressed[K_RIGHT] or keys_pressed[K_d]) and self.ship:
            self.ship.rotate(3)
        if (keys_pressed[K_UP] or keys_pressed[K_w]) and self.ship:
            self.ship.accelerate(0.05)
        if (keys_pressed[K_DOWN] or keys_pressed[K_s]) and self.ship:
            self.ship.accelerate(0)
        if keys_pressed[K_SPACE] and self.ship:
            # TODO: should create a bullet when the user fires
            if len(self.bullets) == 0:
                self.bullets.append(Bullet(self.ship.get_x(), self.ship.get_y(), self.ship.get_rotation()))
                


    def update_simulation(self):

        """
        update_simulation() causes all objects in the game to update themselves
        """


        super().update_simulation()

        if self.ship:
            self.ship.update( self.width, self.height )

        for asteroid in self.asteroids:
            asteroid.update( self.width, self.height )
            if len(self.asteroids) < 8:
                self.asteroids.append(Stones(True))

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
            if asteriod.collide(self.ship):
                    self.asteroids.remove(asteriod)

            for bullet in self.bullets:
                if asteriod.contains(bullet.position):
                    self.asteroids.remove(asteriod)
                    self.bullets.remove(bullet)

