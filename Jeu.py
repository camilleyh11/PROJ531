# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:57:01 2020

@author: ruellee
"""

class Jeu:
    def __init__(self):
        self.num=0
        
    def deplacement_tour(self, caseArrivee, caseDepart): #méthode pour déplacer la tour
        #deplacement vertical et horizontal
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        
        return (ligneD==ligneA or colonneD==colonneA)
    
    
    def deplacement_fou(self, caseArrivee, caseDepart):
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        for i in range(0,8,1):
            if ligneA==ligneD-i or ligneA==ligneD+i:
                return (colonneA==colonneD-i or colonneA==colonneD+i)
        return False
    
    def deplacement_reine(self, caseArrivee, caseDepart):
        return self.deplacement_tour(caseArrivee, caseDepart) or self.deplacement_fou(caseArrivee, caseDepart)
    
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
        
    def deplacement_cavalier(self,caseArrivee, caseDepart):
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        if ligneA==ligneD+1 or ligneA==ligneD-1:
            return (colonneA==colonneD+2 or colonneA==colonneD-2)
        if colonneA==colonneD+1 or colonneA==colonneD-1:
            return (ligneA==ligneD+2 or ligneA==ligneD-2)
        
    def deplacement_pion(self,caseArrivee, caseDepart,couleur):
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        if caseDepart.piece.aDejaJoue==True:
            if colonneA==colonneD:
                if couleur =='Blanc':       
                    return ligneA==ligneD-1
                if couleur =='Noir':
                    return ligneA==ligneD+1
                
        if caseDepart.piece.aDejaJoue==False:
            if colonneA==colonneD:
                if couleur =='Blanc':
                    caseDepart.piece.aDejaJoue=True
                    return (ligneA==ligneD-1 or ligneA==ligneD-2)
                if couleur =='Noir':
                    caseDepart.piece.aDejaJoue=True
                    return (ligneA==ligneD+1 or ligneA==ligneD+2)
                
        if caseArrivee.colonne==caseDepart.colonne-1:
            if couleur =='Blanc':
                if caseArrivee.ligne==caseDepart.ligne-1:
                    caseDepart.piece.aDejaJoue=True
                    return (caseArrivee.piece!=None and caseArrivee.piece.couleur=='Noir')
            if couleur=='Noir':
                if caseArrivee.ligne==caseDepart.ligne+1:
                    caseDepart.piece.aDejaJoue=True
                    return (caseArrivee.piece!=None and caseArrivee.piece.couleur=='Blanc')
                
        if caseArrivee.colonne==caseDepart.colonne+1:
            if couleur =='Blanc':
                if caseArrivee.ligne==caseDepart.ligne-1:
                    caseDepart.piece.aDejaJoue=True
                    return (caseArrivee.piece!=None and caseArrivee.piece.couleur=='Noir')
            if couleur=='Noir':
                if caseArrivee.ligne==caseDepart.ligne+1:
                    caseDepart.piece.aDejaJoue=True
                    return (caseArrivee.piece!=None and caseArrivee.piece.couleur=='Blanc')
                    
                    
            
            
        