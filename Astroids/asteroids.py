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

        self.asteroids = []
        for i in range(8):
            self.asteroids.append(Stones(False))
        
        self.stars=[]
        for i in range(100):
            self.stars.append(Star())
        

        self.bullets = []

        self.myfont = pygame.font.SysFont("monospace", 20, True)

        self.life = 3
        self.score = 0
        self.last = pygame.time.get_ticks()
        self.cooldown = 150


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
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.last = now
                if len(self.bullets) <= 10:
                    self.last = now
                    #self.blastSound.play()
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
                self.asteroids.append(Stones())

        #for star in self.stars:
            #star.update( self.width, self.height )

        for bullet in self.bullets:
            if bullet.update(self.width, self.height) == True:
                    self.bullets.remove(bullet)

        self.handle_collisions()

    def render_objects(self):
        """
        render_objects() causes all objects in the game to draw themselves onto the screen
        """
        super().render_objects()


        if self.ship:
            self.ship.draw( self.screen )


        for star in self.stars:
            star.draw( self.screen )


        for asteroid in self.asteroids:
            asteroid.draw( self.screen )

        for bullet in self.bullets:
            bullet.draw( self.screen )

        score = self.myfont.render("Score: {}".format(str(self.score)), 1, (255, 0, 0))
        self.screen.blit(score, (390, 5))

        visible_life = self.life
        if visible_life < 0: visible_life = 0
        life = self.myfont.render("Life: {}".format(str(visible_life)), 1, (255, 0, 0))
        self.screen.blit(life, (50, 5))
        if (self.life < 0):
            Game_Over = self.myfont.render("Game Over", 1, (255, 0, 0))
            self.screen.blit(Game_Over, (250, 250))
            self.ship = None


    def handle_collisions(self):
        """
        handle_collisions() should check:
            - if our ship has crashed into an asteroid (the ship gets destroyed - game over!)
            - if a bullet has hit an asteroid (the asteroid gets destroyed)
        :return: 
        """


        if not self.ship:
            return

        for asteriod in self.asteroids:
            if asteriod.collide(self.ship):
                    self.asteroids.remove(asteriod)
                    self.life = self.life - 1

            for bullet in self.bullets:
                if asteriod.contains(bullet.position):
                    if asteriod.name == "L":
                        self.asteroids.remove(asteriod)
                        #self.asteroids.append(Stones("M"))
                        #Anton har all this med små stenar
                    self.bullets.remove(bullet)
                    self.score += 10
                    #Hur mycket score ska man få per sten yo? o:

