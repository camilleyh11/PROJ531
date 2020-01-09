# -*- coding: utf-8 -*-

class Case:
    
    
    
    #constructeur
    def __init__(self,ligne,colonne,couleur,rect) :
        self.piece=None
        self.colonne=colonne
        self.ligne=ligne
        self.rect=rect # De forme [x,y,longueur, largeur], ici longueur et largeur =75
        self.couleur=couleur # blanc = [255,255,255] ou bleu =[0,200,150]
        
    #Permet de changer la piece sur la case
    def setPiece(self, piece=None):
        self.piece = piece
        
            
     
