# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:57:01 2020

@author: ruellee
"""
from Joueur import Joueur
class Jeu:
    
    #constructeur ( on sait pas si c'est utile)
    def __init__(self):
        self.coupValide=False # Pour savoir si le coup joue est valide
        self.joueur=Joueur('Blanc',1,self,True) # L'humain joue les blancs
        self.ordi=Joueur('Noir',0,self,False) # L'IA joue les noirs
    
###############################################################################
    ''' Deplacements des differentes pieces''' 
    ''' La tour se deplace verticalement et horizontalement'''
    
    def deplacement_tour(self, caseArrivee, caseDepart): 
        #deplacement vertical et horizontal
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        
        return (ligneD==ligneA or colonneD==colonneA)
###############################################################################
        
    ''' Le fou se déplace suivant les diagonales'''
    
    def deplacement_fou(self, caseArrivee, caseDepart):
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        for i in range(0,8,1):
            if ligneA==ligneD-i or ligneA==ligneD+i:
                return (colonneA==colonneD-i or colonneA==colonneD+i)
        return False
    
###############################################################################  
        
    ''' La reine se deplace comme un fou et une tour'''
    
    def deplacement_reine(self, caseArrivee, caseDepart):
        return self.deplacement_tour(caseArrivee, caseDepart) or self.deplacement_fou(caseArrivee, caseDepart)
    
###############################################################################    
    
    ''' Le roi se deplace comme une reine mais seulement d'une case'''
    
    def deplacement_roi(self, caseArrivee, caseDepart):
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        DepHorizon=False
        DepVertical=False
        DepDiag=False
        if ligneD==ligneA:
            DepHorizon=colonneA==colonneD+1 or colonneA==colonneD-1
        if colonneD==colonneA:
            DepVertical=ligneA==ligneD+1 or ligneA==ligneD-1
        if ligneA==ligneD-1 or ligneA==ligneD+1:
                DepDiag=(colonneA==colonneD-1 or colonneA==colonneD+1)
                
        if DepHorizon or DepVertical or DepDiag:
            return True
        
###############################################################################       
            
    ''' le roi se deplace soit d'une colonne puis de 2 lignes soit 
     d'une ligne puis deux colonnes'''
     
    def deplacement_cavalier(self,caseArrivee, caseDepart):
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        if ligneA==ligneD+1 or ligneA==ligneD-1:
            return (colonneA==colonneD+2 or colonneA==colonneD-2)
        if colonneA==colonneD+1 or colonneA==colonneD-1:
            return (ligneA==ligneD+2 or ligneA==ligneD-2)
        
###############################################################################     
            
    ''' Le pion ne peut qu'avancer de deux cases (si c'est le premier deplacement)
     ou d'une seule case''' 
    
    def deplacement_pion(self,caseArrivee, caseDepart,couleur):
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        # Si le pion s'est deja deplace, alors il ne peut bouger que 
        # d'une seule case 
        if caseDepart.piece.aDejaJoue==True:
            if colonneA==colonneD:
                # Le pion blanc "monte" d'une case l'echiquier
                if couleur =='Blanc':       
                    return ligneA==ligneD-1
                # Le pion noir "descend" l'echiquier
                if couleur =='Noir':
                    return ligneA==ligneD+1
        # Si le pion ne s'est pas encore deplace, il peut se deplacer soit
        # de deux cases, soit d'une seule case
        if caseDepart.piece.aDejaJoue==False:
            if colonneA==colonneD:
                # Le pion blanc "monte" l'echiquier d'une ou de deux cases
                if couleur =='Blanc':
                    caseDepart.piece.aDejaJoue=True
                    return (ligneA==ligneD-1 or ligneA==ligneD-2)
                # Le pion noir "descend" l'echiquier d'une ou de deux cases
                if couleur =='Noir':
                    caseDepart.piece.aDejaJoue=True
                    return (ligneA==ligneD+1 or ligneA==ligneD+2)
          
        # Le pion mange en diagonal, il faut donc verifier qu'une piece
        # d'une couleur différente se trouve sur la case en diagonale
        
        # Deplacement sur la diagonale gauche de l'echiquier 
        if caseArrivee.colonne==caseDepart.colonne-1:
            if couleur =='Blanc':
                if caseArrivee.ligne==caseDepart.ligne-1:
                    caseDepart.piece.aDejaJoue=True
                    return (caseArrivee.piece!=None and caseArrivee.piece.couleur=='Noir')
            if couleur=='Noir':
                if caseArrivee.ligne==caseDepart.ligne+1:
                    caseDepart.piece.aDejaJoue=True
                    return (caseArrivee.piece!=None and caseArrivee.piece.couleur=='Blanc')
                
        # Deplacement sur la diagonale droite de l'echiquier 
        if caseArrivee.colonne==caseDepart.colonne+1:
            if couleur =='Blanc':
                if caseArrivee.ligne==caseDepart.ligne-1:
                    caseDepart.piece.aDejaJoue=True
                    return (caseArrivee.piece!=None and caseArrivee.piece.couleur=='Noir')
            if couleur=='Noir':
                if caseArrivee.ligne==caseDepart.ligne+1:
                    caseDepart.piece.aDejaJoue=True
                    return (caseArrivee.piece!=None and caseArrivee.piece.couleur=='Blanc')
                    
                    
    def miseDangerRoi(self,case):
        print(case.ligne)
        
###############################################################################
    ''' JOUER UN COUP'''
###############################################################################
    
    '''Verifie qui doit jouer et deplace la piece si le coup demande et valide
    sinon le joueur doit jouer jusqu'a tant que le coup soit valide'''
    
    def joue(self,caseDepart,caseArrivee,echiquier):
                #Si l'humain doit jouer
                if self.joueur.joue:
                    # Si il clique sur une case de l'echiquier et qu'il y a une piece
                    if caseDepart != None and caseDepart.piece!=None:
                        # Si la piece selectionnee est de sa couleur
                        if caseDepart.piece.couleur==self.joueur.couleur:
                                self.deplacementPiece(caseDepart,caseArrivee,echiquier)
                                # Si le coup est valide, on change de joueur
                                #et on remet coupValide a False
                                if self.coupValide:
                                    self.joueur.setJoue(False)
                                    self.ordi.setJoue(True)
                                    self.coupValide=False
                                    
                #Si l'ordi doit jouer
                else:
                    # Si il clique sur une case de l'echiquier et qu'il y a une piece
                    if caseDepart != None and caseDepart.piece!=None:
                        # Si la piece selectionnee est de sa couleur
                        if caseDepart.piece.couleur==self.ordi.couleur:
                                self.deplacementPiece(caseDepart,caseArrivee,echiquier)
                                # Si le coup est valide, on change de joueur
                                #et on remet coupValide a False
                                if self.coupValide:
                                    self.ordi.setJoue(False)
                                    self.joueur.setJoue(True)
                                    self.coupValide=False
    #    def miseDangerRoi(self,case):
    #        return case.ligne
        
    ''' Deplace la piece selectionee '''
    
    def deplacementPiece(self,caseDepart,caseArrivee,echiquier):
        
        # Si la caseDepart est sur l'echiquier et qu'il y a une piece
        if caseDepart!=None and caseDepart.piece!=None:
            pieceD= caseDepart.piece
            
            # Si caseArrivee est sur l'echiquier et 
            # (si il n'y a pas de piece ou si il y a une piece d'une couleur differente) et 
            # si il n'y a pas d'obstacle sur la trajectoire de la piece deplacee
            if caseArrivee!=None and (caseArrivee.piece== None or caseArrivee.piece.couleur!=pieceD.couleur)and self.verifObstacle(pieceD.nom,pieceD.couleur,caseDepart,caseArrivee,echiquier):
                if pieceD.nom=='Tour':
                    if self.deplacement_tour(caseArrivee,caseDepart):
                        self.coupValide=True
                        caseDepart.setPiece()
                        caseArrivee.setPiece(pieceD)
                if pieceD.nom=='Fou':
                    if self.deplacement_fou(caseArrivee,caseDepart):
                        self.coupValide=True
                        caseDepart.setPiece()
                        caseArrivee.setPiece(pieceD)
                if pieceD.nom=='Reine':
                    if self.deplacement_reine(caseArrivee,caseDepart):
                        self.coupValide=True
                        caseDepart.setPiece()
                        caseArrivee.setPiece(pieceD)
                        
                if pieceD.nom=='Roi':
                    if self.deplacement_roi(caseArrivee,caseDepart):
                        self.coupValide=True
                        caseDepart.setPiece()
                        caseArrivee.setPiece(pieceD)
                        
                if pieceD.nom=='Cavalier':
                    if self.deplacement_cavalier(caseArrivee,caseDepart):
                        self.coupValide=True
                        caseDepart.setPiece()
                        caseArrivee.setPiece(pieceD)
                        
                if pieceD.nom =='Pion' and self.verifObstacle(pieceD.nom,pieceD.couleur,caseDepart,caseArrivee,echiquier) :
                    if self.deplacement_pion(caseArrivee,caseDepart,caseDepart.piece.couleur):
                        self.coupValide=True
                        caseDepart.setPiece()
                        caseArrivee.setPiece(pieceD)
    
    
    ''' On verifie que la piece passee en parametre peut jouer le coup,
    qu'il n'y a pas d'autre piece sur sa trajectoire.
    Si la piece peut, on retourne True et sinon False'''
            
    def verifObstacle(self,nom,couleur,caseDepart,caseArrivee,echiquier):
        
        if nom=='Tour':
            return self.verifObstacleTour(echiquier,caseDepart,caseArrivee)
        
        if nom=='Fou':
            return self.verifObstacleFou(echiquier,caseDepart,caseArrivee)
        
        #Le roi et la reine se deplace comme le Fou et la Tour
        if nom=='Reine' or nom=='Roi':
            if caseArrivee.ligne==caseDepart.ligne or caseArrivee.colonne==caseDepart.colonne:
                return self.verifObstacleTour(echiquier,caseDepart,caseArrivee)
            else:
                return self.verifObstacleFou(echiquier,caseDepart,caseArrivee)
            
        # Le pion blanc "monte" le plateau de jeu  
        if nom=='Pion' and couleur=='Blanc': 
            if caseArrivee.colonne==caseDepart.colonne:
                #le pion peut se deplacer d'une ou deux cases
                for i in range(caseArrivee.ligne,caseDepart.ligne,1):
                    if echiquier.jeu[i][caseDepart.colonne].piece!=None:
                                return False
        
        # Le pion noir "descend" le plateau de jeu
        if nom=='Pion' and couleur=='Noir': 
            if caseArrivee.colonne==caseDepart.colonne:
                #le pion peut se deplacer d'une ou deux cases
                for i in range(caseDepart.ligne+1,caseArrivee.ligne+1,1):
                    if echiquier.jeu[i][caseDepart.colonne].piece!=None:
                                return False
        return True
             
                 
    ''' On verifie que la Tour peut jouer le coup,
    qu'il n'y a pas d'autre piece sur sa trajectoire
    Si la piece peut, on retourne True et sinon False'''
        
    def verifObstacleTour(self,echiquier,caseDepart,caseArrivee):
            if caseArrivee.ligne==caseDepart.ligne:
                if caseArrivee.colonne-caseDepart.colonne>0:
                    for i in range(caseDepart.colonne+1,caseArrivee.colonne,1):
                        if echiquier.jeu[caseArrivee.ligne][i].piece!=None:
                            return False
                else:
                    for i in range(caseArrivee.colonne+1,caseDepart.colonne,1):
                        if echiquier.jeu[caseArrivee.ligne][i].piece!=None:
                            return False
                        
                        
            if caseArrivee.colonne==caseDepart.colonne:
                
                if caseArrivee.ligne-caseDepart.ligne>0:
                    for i in range(caseDepart.ligne+1,caseArrivee.ligne,1):
                        if echiquier.jeu[i][caseArrivee.colonne].piece!=None:
                            return False
                else:
                    for i in range(caseArrivee.ligne+1,caseDepart.ligne,1):
                        if echiquier.jeu[i][caseArrivee.colonne].piece!=None:
                            return False
            return True
                
    ''' On verifie que le Fou peut jouer le coup,
    qu'il n'y a pas d'autre piece sur sa trajectoire
    Si la piece peut, on retourne True et sinon False'''
        
    def verifObstacleFou(self,echiquier,caseDepart,caseArrivee):
        ligneD=caseDepart.ligne
        ligneA=caseArrivee.ligne
        if caseArrivee.colonne-caseDepart.colonne>0:
            if caseArrivee.ligne-caseDepart.ligne>0:
                for colonne in range(caseDepart.colonne+1,caseArrivee.colonne,1):
                    ligneD=ligneD+1
                    if echiquier.jeu[ligneD][colonne].piece!=None:
                        return False
            else:
                for colonne in range(caseDepart.colonne+1,caseArrivee.colonne,1):
                        ligneD=ligneD-1
                        if echiquier.jeu[ligneD][colonne].piece!=None:
                            return False
        else:
            if caseArrivee.ligne-caseDepart.ligne>0:
                for colonne in range(caseArrivee.colonne,caseDepart.colonne,1):
                    if echiquier.jeu[ligneA][colonne].piece!=None:
                        
                        return False
                    ligneA=ligneA-1
            else:
                for colonne in range(caseArrivee.colonne,caseDepart.colonne,1):
                    if echiquier.jeu[ligneA][colonne].piece!=None:
                        return False          
                    ligneA=ligneA+1 
        return True
            
        