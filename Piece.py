# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:40:50 2020

@author: elsar
"""
class Piece:
    
    #constructeur
    def __init__(self,couleur,nom,rect,num=None,aDejaJoue=None):
        self.couleur=couleur # Blanc ou Noir
        self.nom=nom # Pion, Roi, Reine, Tour, Fou ou Cavalier
        self.rect=rect # De forme [x,y,longueur, largeur], ici longueur et largeur =75
        self.num=num #inutile pour l'instant
        
        #pour le pion
        self.aDejaJoue=aDejaJoue
    
        
        