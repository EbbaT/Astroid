import sys, os
import pygame
from pygame.locals import *

from abc import ABC, abstractmethod

class Game( ABC ):
    """
    Game is an abstract base class to manage basic game concepts
    """
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

        # Running game state
        self.running = True

        # Keep track of how many times we have drawn a frame in the game:
        self.frame = 0
        self.forth = 0

        # create graphical frame
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption(name)
        pygame.init()

        # Store the screen object for drawing too
        self.screen = pygame.display.set_mode([width,height])

        self.dashboard = pygame.image.load("dashboard.png")
        self.dashboard = pygame.transform.scale(self.dashboard, (width, 60))
        self.blastSound = pygame.mixer.Sound("blaster.wav")

        self.myfont = pygame.font.SysFont("monospace", 20, True)
        self.smallFont = pygame.font.SysFont("monospace", 13, True)
        self.info = self.smallFont.render("Press [i] at any time to show information", 1, (255, 255, 255))


    def runGame(self):
        # Our "infinite" loop for the game logic and drawing
        while self.running:
            # WARNING: the following code is very important, if we don't loop
            # through all the events then the game window will never be drawn!
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()
            self.update_simulation()
            self.paint()
        pygame.quit()

    def paint(self):
        self.screen.fill( (0,0,0) )
        self.screen.blit(self.dashboard, (0, 0))
        self.render_objects()
        
        self.screen.blit(self.info, (20, 575))
        pygame.display.flip()

    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_q]:
            print("User initiated a QUIT")
            self.running = False  # So the user can close the program

        if keys_pressed[K_r]:
            #self.running = False
            self.__init__(self.name, self.width, self.height)
            self.running = True
            self.runGame()

        if keys_pressed[K_i]:
            #Ska visa textFil.txt
            pass


    def update_simulation(self):
        self.frame += 1
        self.forth += 1

    @abstractmethod
    def render_objects(self):
        pass








