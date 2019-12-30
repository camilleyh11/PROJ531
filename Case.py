# -*- coding: utf-8 -*-

class Case:
    
    #constructeur
    def __init__(self,ligne,colonne,couleur,rect) :
        self.piece=None
        self.colonne=colonne
        self.ligne=ligne
        self.rect=rect
        self.couleur=couleur
        
    #Permet de changer la piece sur la case
    def setPiece(self, piece):
        self.piece = piece
        
            
     
