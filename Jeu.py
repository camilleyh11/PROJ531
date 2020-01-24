# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:57:01 2020
@author: ruellee
"""
import random
from Joueur import Joueur
class Jeu:
    
    #constructeur ( on sait pas si c'est utile)
    def __init__(self):
        self.coupValide=False # Pour savoir si le coup joue est valide
        self.joueur=Joueur('Blanc',1,self,True) # L'humain joue les blancs
        self.ordi=Joueur('Noir',0,self,False) # L'IA joue les noirs
        self.pat=False #On initialise le pat à faux
    
    #on recupere le joueur qui joue 
    def getJoueur(self):
        if self.joueur.joue==True:
            return self.joueur
        else:
            return self.ordi
    
    def getJoueurAdverse(self):
        if self.joueur.joue==False:
            return self.joueur
        else:
            return self.ordi
    
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
        return False
        
###############################################################################       
            
    ''' le cavalier se deplace soit d'une colonne puis de 2 lignes soit 
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
        return False
        
###############################################################################     
            
    '''Soit le pion peut manger une piece adverse qui est dans sa diagonale
    sinon le pion se deplace'''
    
    def deplacement_pion(self,caseArrivee, caseDepart,couleur,echiquier):
        mange=False
        avance=False
        #le pion mange si une piece si la case arrivee possede une piece adverse
        if caseArrivee.piece!=None and caseArrivee.piece.couleur!=couleur:
            mange=self.pionMangePiece(caseArrivee, caseDepart,couleur)
        #sinon le pion avance
        else:
            avance=self.pionAvance(caseArrivee, caseDepart,couleur)
        #return true si le pion avance ou mange          
        return avance or mange
        
    ''' Le pion ne peut qu'avancer de deux cases (si c'est le premier deplacement)
     ou d'une seule case. Retourne True si le pion peut avancer''' 
    
    def pionAvance(self,caseArrivee, caseDepart,couleur):
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
                    #caseDepart.piece.aDejaJoue=True
                    return (ligneA==ligneD-1 or ligneA==ligneD-2)
                # Le pion noir "descend" l'echiquier d'une ou de deux cases
                if couleur =='Noir':
                    #caseDepart.piece.aDejaJoue=True

                    return (ligneA==ligneD+1 or ligneA==ligneD+2)
        return False
        
                    
        '''Le pion mange en diagonal, il faut donc verifier qu'une piece
         d'une couleur différente se trouve sur la case en diagonale. 
         Retourne True si le pion peut manger en diagonal'''
        
    def pionMangePiece(self,caseArrivee, caseDepart,couleur):      
        # Deplacement sur la diagonale gauche de l'echiquier 
        if caseArrivee.colonne==caseDepart.colonne-1:
            if couleur =='Blanc':
                if caseArrivee.ligne==caseDepart.ligne-1:
                    caseDepart.piece.aDejaJoue=True
                    return True
            if couleur=='Noir':
                if caseArrivee.ligne==caseDepart.ligne+1:
                    caseDepart.piece.aDejaJoue=True
                    return True
                
        # Deplacement sur la diagonale droite de l'echiquier 
        if caseArrivee.colonne==caseDepart.colonne+1:
            if couleur =='Blanc':
                if caseArrivee.ligne==caseDepart.ligne-1:
                    caseDepart.piece.aDejaJoue=True
                    return True
            if couleur=='Noir':
                if caseArrivee.ligne==caseDepart.ligne+1:
                    caseDepart.piece.aDejaJoue=True
                    return True
        return False
        
###############################################################################
    ''' JOUER UN COUP'''
###############################################################################
    
    '''Verifie qui doit jouer et deplace la piece si le coup demande et valide
    sinon le joueur doit jouer jusqu'a tant que le coup soit valide'''
    

    
    
    def joue(self,caseDepart,caseArrivee,echiquier):
        if caseDepart != None and caseDepart.piece!=None:
            joueur=self.getJoueur()
            adversaire=self.getJoueurAdverse()
            if self.echecPat(echiquier):
                self.pat=True
                pass
            if self.echecEtMat(echiquier):
                pass
                #pygame.quit()
            # Si il clique sur une case de l'echiquier et qu'il y a une piece
            if caseDepart != None and caseDepart.piece!=None:
                # Si la piece selectionnee est de sa couleur
                if caseDepart.piece.couleur==joueur.couleur:
                    if not self.estAttaque(echiquier):
                        if caseDepart.piece.nom=='Roi':
                            if not self.seMetEnDanger(echiquier,joueur,caseArrivee):
                                if self.deplacementPiecePossible(caseDepart,caseArrivee,echiquier):
                                    if self.coupValide:
                                        if joueur==self.joueur:
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                                            self.coupAleatoire(echiquier)
                                        if joueur==self.ordi:
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                        else:
                            if self.deplacementPiecePossible(caseDepart,caseArrivee,echiquier):
                                # Si le coup est valide, on change de joueur
                                #et on remet coupValide a False
                                if self.coupValide:
                                    if joueur==self.joueur:
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
#                                            if caseArrivee.piece.nom=='Pion':
#                                                
#                                                if caseArrivee.piece.couleur=='Blanc':
#                                                    if caseArrivee.ligne==0:
#                                                        caseArrivee.setPiecePromotion(echiquier,'Blanc')
                                                        
                                            self.coupAleatoire(echiquier)
                                            
                                    if joueur==self.ordi:
                                        self.deplacementPiece(caseDepart,caseArrivee)
                                        joueur.setJoue(False)
                                        adversaire.setJoue(True)
#                                        if caseArrivee.piece.nom=='Pion':
#                                            if caseArrivee.piece.couleur=='Noir':
#                                                    if caseArrivee.ligne==7:
#                                                        caseArrivee.setPiecePromotion(echiquier,'Noir')
                                        
                    else:
                        if caseDepart.piece.nom=='Roi':
                            if self.seMetEnDanger(echiquier,joueur,caseArrivee)==False:
                                if self.deplacementPiecePossible(caseDepart,caseArrivee,echiquier):
                                    if self.coupValide:                       
                                        if joueur==self.joueur:
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                                            self.coupAleatoire(echiquier)
                                        if joueur==self.ordi:
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                            else:
                                if joueur==self.ordi:
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                        else:
                            if joueur==self.joueur:
                                if self.protegeRoi(echiquier,caseDepart,caseArrivee):
                                    joueur.setJoue(False)
                                    adversaire.setJoue(True)
                                    #if caseArrivee.piece.nom=='Pion':
                                                
#                                        if caseArrivee.piece.couleur=='Blanc':
#                                            if caseArrivee.ligne==0:
#                                                caseArrivee.setPiecePromotion(echiquier,'Blanc')
                                    self.coupAleatoire(echiquier)
                            if joueur==self.ordi:
                                if self.protegeRoi(echiquier,caseDepart,caseArrivee):                                  
                                    joueur.setJoue(False)
                                    adversaire.setJoue(True)
#                                    if caseArrivee.piece.nom=='Pion':
#                                            if caseArrivee.piece.couleur=='Noir':
#                                                    if caseArrivee.ligne==7:
#                                                        caseArrivee.setPiecePromotion(echiquier,'Noir')
                                else:
                                    self.coupAleatoire(echiquier)

                            
    def coupAleatoire(self,echiquier):
        listePiece=echiquier.getPieceNoir()
        num=random.randint(0,len(listePiece)-1)
        piece=listePiece[num]
        listeCaseA=self.getDeplacementPossible(echiquier,piece)
        if not self.echecEtMat(echiquier) and not self.echecPat(echiquier):       
            if listeCaseA==[]:
                self.coupAleatoire(echiquier)
            else:
                numCaseA=random.randint(0,len(listeCaseA)-1)
                caseA=listeCaseA[numCaseA]
                caseD=echiquier.getCasePiece(listePiece[num])
                if not self.estAttaque(echiquier):
                    if piece.nom=='Roi':
                            if not self.seMetEnDanger(echiquier,self.ordi,caseA): 
                                self.joue(caseD,caseA,echiquier)
                                #return False
                            else:
                                self.coupAleatoire(echiquier)
                    else:
                        self.joue(caseD,caseA,echiquier)
                        #return False
                else:
                    if piece.nom=='Roi':
                            if not self.seMetEnDanger(echiquier,self.ordi,caseA): 
                                self.joue(caseD,caseA,echiquier)
                                #return False
                            else:
                                self.coupAleatoire(echiquier)
                    else:
                        if self.protegeRoi(echiquier,caseD,caseA):
                            self.joue(caseD,caseA,echiquier)
                            #return False
                        else:                        
                            self.coupAleatoire(echiquier)
                    
        else:
            return True
        
                        
                        
                                    
    def deplacementPiece(self,caseDepart,caseArrivee):
        if caseArrivee !=None:
            if caseDepart.piece.nom=='Pion':
                caseDepart.piece.aDejaJoue=True
            pieceD=caseDepart.piece
            caseDepart.setPiece()
            caseArrivee.setPiece(pieceD)
        self.coupValide=False
        
    ''' Deplace la piece selectionee '''
    
    def deplacementPiecePossible(self,caseDepart,caseArrivee,echiquier):
        # Si la caseDepart est sur l'echiquier et qu'il y a une piece
        if caseDepart!=None and caseDepart.piece!=None:
            pieceD= caseDepart.piece

            # Si caseArrivee est sur l'echiquier et 
            # (si il n'y a pas de piece ou si il y a une piece d'une couleur differente) et 
            # si il n'y a pas d'obstacle sur la trajectoire de la piece deplacee
            if caseArrivee!=None and (caseArrivee.piece== None or caseArrivee.piece.couleur!=pieceD.couleur)and self.verifObstacle(pieceD.nom,pieceD.couleur,caseDepart,caseArrivee,echiquier):
                    
                    if pieceD.nom=='Tour':
                        self.coupValide=True
                        return self.deplacement_tour(caseArrivee,caseDepart)
                    if pieceD.nom=='Fou':
                        self.coupValide=True
                        return self.deplacement_fou(caseArrivee,caseDepart)
                        
                    if pieceD.nom=='Reine':
                        self.coupValide=True
                        return self.deplacement_reine(caseArrivee,caseDepart)
                            
                    if pieceD.nom=='Roi':
                        self.coupValide=True
                        return self.deplacement_roi(caseArrivee,caseDepart)
                            
                    if pieceD.nom=='Cavalier':
                        self.coupValide=True
                        return self.deplacement_cavalier(caseArrivee,caseDepart)
                            
                    if pieceD.nom =='Pion' and self.verifObstacle(pieceD.nom,pieceD.couleur,caseDepart,caseArrivee,echiquier) :

                        self.coupValide=True
                        return self.deplacement_pion(caseArrivee,caseDepart,caseDepart.piece.couleur,echiquier)
                    return False
            return False
        return False
    
    #cette methode permet d'obtenir l'ensemble des deplacements que peut 
    #effectuer une piece passee en parametre
    def getDeplacementPossible(self,echiquier,piece):
        #on cree une liste vide de cases d'arrivee
        listeCaseA=[]
        #on recupere la case de départ grace au getter
        caseD=echiquier.getCasePiece(piece)
        #on parcourt l'echiquier
        for ligne in echiquier.jeu:
            for case in ligne:
                #si la piece peut se deplacer
                if self.deplacementPiecePossible(caseD,case,echiquier):
                    #on ajoute la case arrivee dans la liste des cases arrivee
                   listeCaseA.append(case) 
        return listeCaseA
                
            
    
    
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
        if ligneA>=8 and caseArrivee.colonne>=8 and ligneA<0 and caseArrivee.colonne<0:
            return False
        if caseArrivee.colonne-caseDepart.colonne==0 or caseArrivee.ligne-caseDepart.ligne==0:
            return False
        if caseArrivee.colonne-caseDepart.colonne>0:
            if caseArrivee.ligne-caseDepart.ligne>0:
                for colonne in range(caseDepart.colonne+1,caseArrivee.colonne,1):
                    ligneD=ligneD+1
                    if echiquier.jeu[ligneD][colonne].piece!=None:
                        return False
            if caseArrivee.ligne-caseDepart.ligne<0 :
                for colonne in range(caseDepart.colonne+1,caseArrivee.colonne,1):
                        ligneD=ligneD-1
                        if echiquier.jeu[ligneD][colonne].piece!=None:
                            return False
        if caseArrivee.colonne-caseDepart.colonne<0:
            if caseArrivee.ligne-caseDepart.ligne>0:
                for colonne in range(caseArrivee.colonne+1,caseDepart.colonne,1):
                    ligneA=ligneA-1
                    if echiquier.jeu[ligneA][colonne].piece!=None:    
                        return False
                    
            if caseArrivee.ligne-caseDepart.ligne<0:
                for colonne in range(caseArrivee.colonne+1,caseDepart.colonne,1):
                    ligneA=ligneA+1
                    if echiquier.jeu[ligneA][colonne].piece!=None:
                        return False          
        return True
        
            
###############################################################################
        '''MISE EN DANGER DU ROI'''
###############################################################################
    
    #methode pour savoir si l'adversaire peut attaquer le roi
    def adversairePeutAttaquer(self,caseAdverse,caseRoi,echiquier):
        #return true si une piece adverse peut "manger" le roi sinon false
        return self.deplacementPiecePossible(caseAdverse,caseRoi,echiquier)
    
    #methode pour savoir si le roi se met en danger
    def seMetEnDanger(self,echiquier,joueur,futurCaseRoi):
        #on recupere la case du roi
        caseR=echiquier.getCaseRoi(joueur.couleur)
        pieceR=caseR.piece
        caseR.setPiece()
        if joueur.couleur=='Blanc':
            couleur='Noir'
        else:
            couleur='Blanc'
        #si la future case du roi existe
        if futurCaseRoi!=None:
            #on parcourt l'echiquier
            for ligne in echiquier.jeu:
                for case in ligne:
                    #si la case possede une piece d'une couleur differente 
                    #de celle du roi
                    if case.piece!= None and case.piece.couleur!=pieceR.couleur:
                        
                        #si c'est le pion
                        if case.piece.nom=='Pion':
                            if futurCaseRoi.piece!=None:
                                ennemi=futurCaseRoi.piece
                                futurCaseRoi.setPiece(pieceR)
                                if self.pionMangePiece(futurCaseRoi,case,couleur):
                                    caseR.setPiece(pieceR)
                                    futurCaseRoi.setPiece(ennemi)
                                    return True
                                else:
                                    futurCaseRoi.setPiece(ennemi)
                            else:
                                #si le pion pourra manger le roi sur sa future case
                                #alors le roi est en danger -> return true
                                if self.pionMangePiece(futurCaseRoi,case,couleur):
                                    caseR.setPiece(pieceR)
                                    return True
                        #si c'est une autre piece que le pion
                        else:
                            if futurCaseRoi.piece!=None:
                                ennemi=futurCaseRoi.piece
                                futurCaseRoi.setPiece()
                                if self.adversairePeutAttaquer(case,futurCaseRoi,echiquier):
                                    futurCaseRoi.setPiece(ennemi)
                                    caseR.setPiece(pieceR)
                                    return True 
                                
                                if not self.adversairePeutAttaquer(case,futurCaseRoi,echiquier):
                                    futurCaseRoi.setPiece(ennemi)
                            #on appelle adversairePeutAttaquer, si True alors 
                            #le roi est en danger -> return true
                            if futurCaseRoi.piece==None:
                                if self.adversairePeutAttaquer(case,futurCaseRoi,echiquier):
                                    caseR.setPiece(pieceR)
                                    return True
        #le roi n'est pas en danger on retourne false
        caseR.setPiece(pieceR)
        return False
    
    #methode qui retourne vrai si le deplacement de la piece permet de proteger le roi
    def protegeRoi(self,echiquier,caseDepart,caseArrivee):  
        #si le deplacement de la piece choisie est possible
        if self.deplacementPiecePossible(caseDepart,caseArrivee,echiquier):
            # Si le coup est valide
            if self.coupValide:
                #on deplace la piece
                self.deplacementPiece(caseDepart,caseArrivee)
                #si le roi est attaque
                if self.estAttaque(echiquier):
                    #on remet la piece a son ancienne place
                    self.deplacementPiece(caseArrivee,caseDepart)
                    return False
                return True
        
    #methode qui permet de savoir si le roi est attaque
    def estAttaque(self,echiquier):
        #on recupere le joueur
        joueur=self.getJoueur()
        #on recupere le roi du joueur
        caseRoi=echiquier.getCaseRoi(joueur.couleur)
        #on retourne true si le roi est en dange sur sa case actuelle
        #sinon on retourne false
        return self.seMetEnDanger(echiquier,joueur,caseRoi)
        
   #methode qui permet de savoir si le roi est en echec 
    def echecRoi(self,echiquier):
        #on recupere la case du roi du joueur
        caseR=echiquier.getCaseRoi(self.getJoueur().couleur)
        #si le roi est attaque
        if self.estAttaque(echiquier):
            #on parcourt les cases qui sont autour du roi (les cases sur 
            #lesquelles il peut se deplacer)              
            for ligne in range(caseR.ligne-1,caseR.ligne+2,1):
                for colonne in range(caseR.colonne-1,caseR.colonne+2,1):
                    if ligne<8 and colonne <8 and ligne>=0 and colonne>=0:   
                        case=echiquier.jeu[ligne][colonne]
                        if case!=caseR:
                            #si la case ne possede pas de pice ou si la case
                            #a une piece adverse
                            if case.piece==None or case.piece.couleur!=caseR.piece.couleur:
                                #si le roi n'est pas en danger -> return false
                                if not self.seMetEnDanger(echiquier,self.getJoueur(),case):
                                    return False
                                
            #si le roi est en danger -> return true                    
            return True
        return False
        
    #methode pour savoir s'il y a echec et mat    
    def echecEtMat(self,echiquier):
        #on recupere le joueur
        joueur=self.getJoueur()
        #si le roi est en echec
        if self.echecRoi(echiquier):
            #on parcourt l'echiquier
            for ligne in echiquier.jeu:
                for case in ligne:
                    if case.piece!= None:
                        if case.piece.couleur==joueur.couleur:
                            for l in echiquier.jeu:
                                for c in l:
                                    #si le roi peut etre protege -> pas d'echec
                                    #et mat -> return false
                                    if self.protegeRoi(echiquier,case,c):
                        
                                        return False
            #si le roi ne peut pas etre protege alors echec et mat -> true                        
            return True
        #si le roi n'est pas en echec -> pas d'echec et mat ->false
        return False
        
        
       
    #methode qui permet de savoir s'il y a pat
    def echecPat(self,echiquier):
        #on recupere le joueur
        joueur=self.getJoueur()
        #si le roi n'est pas en echec
        if not self.echecRoi(echiquier):
            #on parcourt l'echiquier
            for ligne in echiquier.jeu:
                for case in ligne:
                    if case.piece!=None:
                        if case.piece.couleur==joueur.couleur:
                            for l in echiquier.jeu:
                                for c in l:
                                    #si la case est le roi
                                    if case.piece.nom=='Roi':
                                        #si le roi peut se deplacer
                                        if self.deplacementPiecePossible(case,c,echiquier):
                                            #si le roi ne se met pas en danger
                                            if not self.seMetEnDanger(echiquier,joueur,c):
                                                #il n'y a pas de pat -> false
                                                return False
                                    #si ce n'est pas le roi        
                                    else:
                                        #si on peut deplacer la piece -> pas de pat false
                                        if self.deplacementPiecePossible(case,c,echiquier):
                                            return False
            #si on ne peut plus bouger le roi sans qu'il se mette en danger
            #donc s'il n'y a plus de deplacement possible alors pat -> true                            
            return True
        #si le roi est en echec -> false
        return False   
        