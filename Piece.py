# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:40:50 2020

@author: elsar
"""
class Piece:
    
    def __init__(self,couleur,nom,rect,num=None,aDejaJoue=None):
        self.couleur=couleur
        self.nom=nom
        self.rect=rect
        self.num=num
        self.aDejaJoue=aDejaJoue
    
        
        