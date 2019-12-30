# -*- coding: utf-8 -*-
import pygame
from Case import Case

class Echiquier:
    
    # Constructeur
    def __init__(self) :
        self.initPygame()
        self.jeu=[]
        self.caseLongueur=75
        self.caseLargeur=75
        self.caseDepart=None
        self.caseArrivee=None
        self.deplacement=None
        #self.joueur=Joueur()
        
        
    # Initializes pygame        
    def initPygame(self): 
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)    
        # Sets the timer to check event every 20 ms
        pygame.time.set_timer(pygame.USEREVENT, 20)         
        # Gets pygame screen
        self.screen = pygame.display.get_surface() 
        
        
        
    # On cree une matrice de 64 case de 8 lignes et 8 colonnes
    def creationJeu(self):
        
        # On recupere la position de la premiere case
        position=self.getPositionCase1()
        
        # i represente les lignes 
        for ligne in range(8):
            # j represente les colonnes
            for colonne in range(8): 
        
                # On calcule la position de la case en fonction de la premiere
        
                x=position[0]+colonne*self.caseLongueur
                y=position[1]+ligne*self.caseLargeur
                
                #on recupere la couleur
                couleur=self.caseCouleur(ligne,colonne)
            
                self.jeu.append([Case(ligne,colonne,couleur,[x,y,self.caseLongueur,self.caseLargeur])])
       
     # Position de la premiere case, on recupere la taille de l'ecran de jeu que l'on divise par 2.
    # On a donc la moitie de l'ecran. On enleve ensuite 4 cases à cette valeur (en x et en y) 
    #pour avoir x1 et y1 de la premiere case 
    
    def getPositionCase1(self):
        x=(self.screen.get_width()//2)-4*self.caseLongueur
        y=(self.screen.get_height()//2)-4*self.caseLargeur
        return [x,y]
        
    
    
    def caseCouleur(self,ligne,colonne):
        
        # Si le numero de la ligne est un nombre pair
        if ligne%2==0:
            
            # Si le numero de la colonne est un nombre pair alors on dessine 
            # un rectangle blanc de longueur et largeur = 95
            if colonne%2==0:
                return [255,255,255]
                
            # Si le numero de la colonne est un nombre impair alors on dessine 
            # un rectangle bleu de longueur et largeur = 95
            if colonne%2==1:
                return [0,200,150]
         
        # Si le numero de la ligne est un nombre impair
        if ligne%2==1:
            
            # Si le numero de la colonne est un nombre impair alors on dessine 
            # un rectangle blanc de longueur et largeur = 95
            if colonne%2==1:
                return [255,255,255]
                
            # Si le numero de la colonne est un nombre pair alors on dessine 
            # un rectangle bleu de longueur et largeur = 95
            if colonne%2==0:
                return [0,200,150]
            
            
            
            
            
            
            
                
    def mouseButtonDown(self,coord):
        self.caseDepart=self.getCase(coord)
        self.deplacement=coord

        
    def mouseButtonUp(self,coord):
        self.caseArrivee=self.getCase(coord)
        self.caseDepart=None

        
    def mouseMotion(self,coord):
        self.deplacement=coord
       
    
    #Renvoie la case correspondant à la position en pixel ou renvoie null si
    #les coordonnées sont hors du plateau de jeu
    def getCase(self,position):
        for ligne in self.jeu:
            for case in ligne:
                rectangle=case.rect
                
                if (position[0]>rectangle[0] and
                    position[0]<rectangle[0]+rectangle[2] and
                    position[1]>rectangle[1] and
                    position[1]<rectangle[1]+rectangle[3]):
                    
                    return case
        return None
                    
                
                    
            
    
    
    
    
    
    
    
    
            
    # Permet d'afficher les cases de l'echiquier
    def display(self):
        #efface l'ecran en noir
        pygame.draw.rect(self.screen,[0,0,0],[0,0,self.screen.get_width(),self.screen.get_height()],0)
                    
        # dessine l'echiquier
        for ligne in self.jeu:
            for case in ligne:
                self.drawCase(case) 
        if self.caseDepart!=None:
            img = pygame.image.load("45px-Chess_kdt45.png")
            img = pygame.transform.scale(img, (75, 75))
            self.screen.blit(img, (self.deplacement[0]-75//2,self.deplacement[1]-75//2))
            
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
                
    
    #dessine les cases de l'echiquier
    def drawCase(self,case):
        
        pygame.draw.rect(self.screen, case.couleur,case.rect, 0)
                
