# -*- coding: utf-8 -*-
import pygame
from Piece import Piece

class Case:
    
    #constructeur
    def __init__(self,colonne,ligne,echiquier,Piece=Piece()) :
        self.piece=Piece
        self.longeur=95
        self.largeur=95
        self.colonne=colonne
        self.ligne=ligne
        self.echiquier=echiquier
        
    #Permet de changer la piece sur la case
    def setPiece(self, piece):
        self.piece = piece
        
        
    # Position de la premiere case, on recupere la taille de l'ecran de jeu que l'on divise par 2.
    # On a donc la moitie de l'ecran. On enleve ensuite 4 cases à cette valeur (en x et en y) 
    #pour avoir x1 et y1 de la premiere case 
    
    def getPosition1(self):
        x=(self.echiquier.screen.get_width()//2)-4*self.longeur
        y=(self.echiquier.screen.get_height()//2)-4*self.largeur
        return [x,y]

    
    #dessine les cases de l'echiquier
    def draw(self):
        
        # On recupere la position de la premiere case
        position=self.getPosition1()
        
        # On calcule la position de la case en fonction de la premiere
        
        x=position[0]+self.colonne*self.longeur
        y=position[1]+self.ligne*self.largeur
        
        # Si le numero de la ligne est un nombre pair
        if self.ligne%2==0:
            
            # Si le numero de la colonne est un nombre pair alors on dessine 
            # un rectangle blanc de longueur et largeur = 95
            if self.colonne%2==0:
                pygame.draw.rect(self.echiquier.screen, [255,255,255],[x,y,self.largeur,self.longeur], 0)
                
            # Si le numero de la colonne est un nombre impair alors on dessine 
            # un rectangle bleu de longueur et largeur = 95
            if self.colonne%2==1:
                pygame.draw.rect(self.echiquier.screen, [0,200,150],[x,y,self.largeur,self.longeur], 0)
         
        # Si le numero de la ligne est un nombre impair
        if self.ligne%2==1:
            
            # Si le numero de la colonne est un nombre impair alors on dessine 
            # un rectangle blanc de longueur et largeur = 95
            if self.colonne%2==1:
                pygame.draw.rect(self.echiquier.screen, [255,255,255],[x,y,self.largeur,self.longeur], 0)
                
            # Si le numero de la colonne est un nombre pair alors on dessine 
            # un rectangle bleu de longueur et largeur = 95
            if self.colonne%2==0:
                pygame.draw.rect(self.echiquier.screen, [0,200,150],[x,y,self.largeur,self.longeur], 0)

    
            
            
     
        
            
        
