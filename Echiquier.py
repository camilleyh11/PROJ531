# -*- coding: utf-8 -*-
import pygame
from Case import Case

class Echiquier:
    
    # Constructeur
    def __init__(self) :
        self.initPygame()
        self.jeu=[]
        #self.joueur=Joueur()
        
    # On cree une matrice de 64 case de 8 lignes et 8 colonnes
    def creationJeu(self):
        
        # i represente les lignes 
        for i in range(8):
            # j represente les colonnes
            for j in range(8):
                self.jeu.append([Case(i,j,self)])
    
        
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
        
        
        
    # Permet d'afficher les cases de l'echiquier
    def display(self):
        
        for i in self.jeu:
            for j in i:
                j.draw() 
            
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
        

       
                