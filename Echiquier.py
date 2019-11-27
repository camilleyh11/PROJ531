# -*- coding: utf-8 -*-
import pygame

class Echiquier:
    # Constructor
    def __init__(self) :
        self.initPygame()
        self.jeu=[]
       
        #self.piece = Piece() 
        #self.joueur=Joueur()
        
    def addCase(self,case):
        case.setJeu(self)
        self.jeu.append(case)
        case.setNum(len(self.jeu))
            
#    def setCase(self,case):
#        self.case=case
#        case.setJeu(self)
#        self.addCase(self,case)
        
    # Initializes pygame        
    def initPygame(self): 
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((1000, 1000))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)         
        # Gets pygame screen
        self.screen = pygame.display.get_surface() 
        
    def display(self):
        # Draws on the screen surface
        self.draw()
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
        
        
    def draw(self):
       for i in range(0,64,1):
           self.jeu[i].draw()
                
        
    def getScreen(self):
        return self.screen
    