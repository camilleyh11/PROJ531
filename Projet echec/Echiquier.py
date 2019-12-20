# -*- coding: utf-8 -*-
import pygame
from Case import Case
from Piece import Piece

class Echiquier:
    
    # Constructeur
    def __init__(self) :
        self.qui_joue='blanc'
        self.initPygame()
        self.jeu=[]
        self.debut=[[Piece('TOUR','noir'),Piece('CAVALIER','noir'),Piece('FOU','noir'),
Piece('DAME','noir'),Piece('ROI','noir'),Piece('FOU','noir'),
Piece('CAVALIER','noir'),Piece('TOUR','noir')],
    
[Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),
Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),
Piece('PION','noir'),Piece('PION','noir')],
 
[Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece()],

[Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece()],

[Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece()],

[Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece()],

[Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),
Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),
Piece('PION','blanc'),Piece('PION','blanc')],
 
 
[Piece('TOUR','blanc'),Piece('CAVALIER','blanc'),Piece('FOU','blanc'),
Piece('DAME','blanc'),Piece('ROI','blanc'),Piece('FOU','blanc'),
Piece('CAVALIER','blanc'),Piece('TOUR','blanc') ]]
        #self.joueur=Joueur()
        
    # On cree une matrice de 64 case de 8 lignes et 8 colonnes
    def creationJeu(self):
        
        # i represente les lignes 
        for i in range(8):
            # j represente les colonnes
            for j in range(8):
                self.jeu.append([Case(i,j,self,self.debut[i][j])])
    
        
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
        
        
#        im=Piece.im_cavalier = pygame.image.load('cavalier.jpg').convert()
#        continuer=True
#        
#        while continuer:
#            self.screen.blit(im,(500,500))
#            for event in pygame.event.get():
#                if event.type==pygame.KEYDOWN:
#                    continuer = False
#            pygame.display.flip()
#        pygame.quit()

        
        
    # Permet d'afficher les cases de l'echiquier
    def display(self):
        
        for i in self.jeu:
            for j in i:
                j.draw() 
            
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
        

       
                