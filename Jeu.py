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
        
    #on recupere le joueur adverse
    def getJoueurAdverse(self):
        if self.joueur.joue==False:
            return self.joueur
        else:
            return self.ordi
    
###############################################################################
    ''' Deplacements des differentes pieces''' 
###############################################################################
    ''' La tour se deplace verticalement et horizontalement'''
    
    def deplacement_tour(self, caseArrivee, caseDepart): 
        #deplacement vertical et horizontal
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        #retourne true que si la ligne de depart est identique a la ligne d'
        #arrivee ou si la colonne de depart est la meme que celle d'arrivee
        return (ligneD==ligneA or colonneD==colonneA)
###############################################################################
        
    ''' Le fou se déplace suivant les diagonales'''
    
    def deplacement_fou(self, caseArrivee, caseDepart):
        ligneA=caseArrivee.ligne
        colonneA=caseArrivee.colonne
        ligneD=caseDepart.ligne
        colonneD=caseDepart.colonne
        for i in range(0,8,1):
            #si la ligne d'arrivee est egale a la ligne de depart + ou - i
            if ligneA==ligneD-i or ligneA==ligneD+i:
                #retourne true si la colonne d'arrivee est egale a la colonne 
                #de depart + ou - i -> ce qui correspond à un deplacement en
                #diagonale
               return (colonneA==colonneD-i or colonneA==colonneD+i)
        #si le deplacement ne correspond pas a un deplacement en diagonale 
        #-> retourne false
        return False
    
###############################################################################  
        
    ''' La reine se deplace comme un fou et une tour'''
    
    def deplacement_reine(self, caseArrivee, caseDepart):
        #on retourne true si le deplacement correspond au deplacement d'une
        #tour ou d'un fou
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
        #si la ligne de depart est indentique a la ligne d'arrivee
        if ligneD==ligneA:
            #alors c'est un deplacemnt horizontal -> sur une meme ligne mais
            #decale à droite ou a gauche d'une colonne
            DepHorizon=colonneA==colonneD+1 or colonneA==colonneD-1
        #si la colonne de depart est identique a celle d'arrivee
        if colonneD==colonneA:
            #le deplacement est vertical, meme colonne -> ligne +ou - 1
            DepVertical=ligneA==ligneD+1 or ligneA==ligneD-1
        #si la ligne d'arrivee correspond a la ligne de depart +ou-1
        if ligneA==ligneD-1 or ligneA==ligneD+1:
                #le deplacement est en diagonal -> ligne +ou-1 et colonne +ou-1 
                DepDiag=(colonneA==colonneD-1 or colonneA==colonneD+1)
        
        #si il y a un deplacement horizontal, vertical ou en diagonal on
        #retourne true sinon false        
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
        #si la ligne d'arrivee est egal a la ligne de depart +ou-1
        if ligneA==ligneD+1 or ligneA==ligneD-1:
            #retourne true si la colonne d'arrivee est egale a +ou-2 la 
            #colonne de depart
            return (colonneA==colonneD+2 or colonneA==colonneD-2)
        #si la colonne d'arrivee est egal a la colonne de depart +ou-1
        if colonneA==colonneD+1 or colonneA==colonneD-1:
            #retourne true si la ligne d'arrivee est egale a +ou-2 la 
            #ligne de depart
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
        #si la case depart existe et si il y a une piece sur la case depart
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
                    #si le roi n'est pas attaque
                    if not self.estAttaque(echiquier):
                        #si la piece deplace est le roi
                        if caseDepart.piece.nom=='Roi':
                            #si son deplacement ne le met pas en danger
                            if not self.seMetEnDanger(echiquier,joueur,caseArrivee):
                                #si le deplacement est possible
                                if self.deplacementPiecePossible(caseDepart,caseArrivee,echiquier):
                                    #si le coup valide est a true
                                    if self.coupValide:
                                        if joueur==self.joueur:
                                            #on deplace la piece
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            #on change la personne qui joue 
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                                            #pour l'ordi on fait un coup aleatoire
                                            self.coupAleatoire(echiquier)
                                        if joueur==self.ordi:
                                            #on deplace la piece
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            #on change la personne qui joue
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                        #si la piece de depart n'est pas un roi
                        else:
                            #si le deplacement de la piece est possible
                            if self.deplacementPiecePossible(caseDepart,caseArrivee,echiquier):
                                # Si le coup est valide,on deplace la piece puis on change de joueur
                                if self.coupValide:
                                    if joueur==self.joueur:
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                                            #pour la promotion
#                                            if caseArrivee.piece.nom=='Pion':
#                                                
#                                                if caseArrivee.piece.couleur=='Blanc':
#                                                    if caseArrivee.ligne==0:
#                                                        caseArrivee.setPiecePromotion(echiquier,'Blanc')
                                            #on provoque un coup aleatoire pour l'ordi           
                                            self.coupAleatoire(echiquier)
                                            
                                    if joueur==self.ordi:
                                        #on deplace la piece puis on change de joueur
                                        self.deplacementPiece(caseDepart,caseArrivee)
                                        joueur.setJoue(False)
                                        adversaire.setJoue(True)
                                        #pour la promotion
#                                        if caseArrivee.piece.nom=='Pion':
#                                            if caseArrivee.piece.couleur=='Noir':
#                                                    if caseArrivee.ligne==7:
#                                                        caseArrivee.setPiecePromotion(echiquier,'Noir')
                    #si le roi n'est pas attaque                    
                    else:
                        #si la piece deplacee est le roi
                        if caseDepart.piece.nom=='Roi':
                            #s'il ne se met pas en danger
                            if self.seMetEnDanger(echiquier,joueur,caseArrivee)==False:
                                #si son deplacement est possible
                                if self.deplacementPiecePossible(caseDepart,caseArrivee,echiquier):
                                    #si le coup est valide on deplace la piece et on change le joueur
                                    if self.coupValide:                       
                                        if joueur==self.joueur:
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                                            #on provoque un coup aleatoire pour l'ordi
                                            self.coupAleatoire(echiquier)
                                        if joueur==self.ordi:
                                            #on deplace la piece et on change le joueur
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                            #si le roi ne se met pas en danger
                            else:
                                if joueur==self.ordi:
                                            #on deplace la piece et on change le joueur
                                            self.deplacementPiece(caseDepart,caseArrivee)
                                            joueur.setJoue(False)
                                            adversaire.setJoue(True)
                        #si la piece deplacee n'est pas le roi
                        else:
                            if joueur==self.joueur:
                                #si la peiece deplacee protege le roi
                                if self.protegeRoi(echiquier,caseDepart,caseArrivee):
                                    joueur.setJoue(False)
                                    adversaire.setJoue(True)
                                    #pour promotion
                                    #if caseArrivee.piece.nom=='Pion':
                                                
#                                        if caseArrivee.piece.couleur=='Blanc':
#                                            if caseArrivee.ligne==0:
#                                                caseArrivee.setPiecePromotion(echiquier,'Blanc')
                                    #pour l'ordi -> coup aleatoire
                                    self.coupAleatoire(echiquier)
                            if joueur==self.ordi:
                                #si le coup protege le roi
                                if self.protegeRoi(echiquier,caseDepart,caseArrivee):                                  
                                    joueur.setJoue(False)
                                    adversaire.setJoue(True)
                                    #pour promotion
#                                    if caseArrivee.piece.nom=='Pion':
#                                            if caseArrivee.piece.couleur=='Noir':
#                                                    if caseArrivee.ligne==7:
#                                                        caseArrivee.setPiecePromotion(echiquier,'Noir')
                                #si le coup ne protege pas le roi on recherche un autre coup    
                                else:
                                    self.coupAleatoire(echiquier)

    #methode pour que l'ordi joue un coup aleatoire                        
    def coupAleatoire(self,echiquier):
        #on recupere la liste des pieces noires (pieces de l'ordi)
        listePiece=echiquier.getPieceNoir()
        #on genere un nombre aleatoire entre 0 et le nombre de pieces presentes 
        #dans la liste
        num=random.randint(0,len(listePiece)-1)
        #on choisi une piece aleatoirement
        piece=listePiece[num]
        #on cree une liste de cases d'arrivee avec les deplacements possibles
        #sur l'echiquier de la piece aleatoire
        listeCaseA=self.getDeplacementPossible(echiquier,piece)
        #si il n'y a pas d'echec et mat ni de pat
        if not self.echecEtMat(echiquier) and not self.echecPat(echiquier):  
            #si la liste de cases d'arrivee est vide -> on rappelle coup aleatoire
            if listeCaseA==[]:
                self.coupAleatoire(echiquier)
            #si la liste n'est pas vide
            else:
                #on cree un numero de case d'arrivee aleatoire entre 0 et la 
                #longueur de la liste des cases d'arrivee
                numCaseA=random.randint(0,len(listeCaseA)-1)
                #on cree une case d'arrivee aleatoire avec le num precedent
                caseA=listeCaseA[numCaseA]
                #la case depart de la piece choisie aleatoirement
                caseD=echiquier.getCasePiece(listePiece[num])
                #si le roi n'est pas attaque
                if not self.estAttaque(echiquier):
                    #si la piece aleatoire est le roi
                    if piece.nom=='Roi':
                            #si il ne se met pas en danger avec so deplacement
                            #alors le deplacement peut etre effectue -> on
                            #appelle joue
                            if not self.seMetEnDanger(echiquier,self.ordi,caseA): 
                                self.joue(caseD,caseA,echiquier)
                                #return False
                            #si il se met en danger -> on cherche un autre coup
                            else:
                                self.coupAleatoire(echiquier)
                    #si la piece joue n'est pas le roi -> on appelle joue
                    else:
                        self.joue(caseD,caseA,echiquier)
                        #return False
                #si le roi est attaque
                else:
                    #si la piece deplacee est le roi
                    if piece.nom=='Roi':
                            #si son deplacement ne le met pas en danger -> joue
                            if not self.seMetEnDanger(echiquier,self.ordi,caseA): 
                                self.joue(caseD,caseA,echiquier)
                                #return False
                            #si son deplacement le met en danger on cherche un
                            #autre coup
                            else:
                                self.coupAleatoire(echiquier)
                    #si la piece deplacee n'est pas le roi
                    else:
                        #si son deplacement protege le roi -> joue
                        if self.protegeRoi(echiquier,caseD,caseA):
                            self.joue(caseD,caseA,echiquier)
                            #return False
                        #sinon on recherche un autre coup possible
                        else:                        
                            self.coupAleatoire(echiquier)
        
        #si il y a echec et mat ou pat -> retourne true            
        else:
            return True
        
                        
                        
    #methode qui permet de deplacer la piece                                
    def deplacementPiece(self,caseDepart,caseArrivee):
        #si la case arrivee existe
        if caseArrivee !=None:
            #si la piece deplacee est le pion
            if caseDepart.piece.nom=='Pion':
                #le pion a deja joue -> est utile pour savoir si le pion peut
                #se deplacer d'1 ou 2 cases
                caseDepart.piece.aDejaJoue=True
            #on recupere la piece sur la case de depart
            pieceD=caseDepart.piece
            #on efface la piece sur la case de depart
            caseDepart.setPiece()
            #on met la piece deplacee sur la case d'arrivee
            caseArrivee.setPiece(pieceD)
        #si la case d'arrivee n'existe pas le coup est faux
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
                    #on ajoute la case arrivee dans la liste des cases d'arrivee
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
            #si la tour se deplace horizontalement
            if caseArrivee.ligne==caseDepart.ligne:
                #si la tour se deplace vers la gauche de l'echiquier
                if caseArrivee.colonne-caseDepart.colonne>0:
                    #on parcourt les cases de la ligne entre la colonne
                    #de depart (+1pour pas que la tour se voit elle meme)
                    #et celle d'arrivee
                    for i in range(caseDepart.colonne+1,caseArrivee.colonne,1):
                        #si l'une des cases possedent une piece -> obstacle
                        #on retourne faux
                        if echiquier.jeu[caseArrivee.ligne][i].piece!=None:
                            return False
                #si la tour se deplace vers la droite
                else:
                    #on parcourt la ligne entre la colonne d'arrivee(+1pour pas  
                    #que la tour se voit elle meme) et celle de depart
                    for i in range(caseArrivee.colonne+1,caseDepart.colonne,1):
                        #si l'une des cases possedent une pice -> obstacle
                        #on retourne faux
                        if echiquier.jeu[caseArrivee.ligne][i].piece!=None:
                            return False
                        
            #si la tour se deplace verticalement           
            if caseArrivee.colonne==caseDepart.colonne:
                #si la ligne d'arrivee est plus grande que la ligne de depart
                if caseArrivee.ligne-caseDepart.ligne>0:
                    #on parcourt la colonne entre la ligne de depart(+1pour pas  
                    #que la tour se voit elle meme)et la ligne d'arrivee 
                    for i in range(caseDepart.ligne+1,caseArrivee.ligne,1):
                        if echiquier.jeu[i][caseArrivee.colonne].piece!=None:
                            return False
                #si la ligne d'arrivee est plus petite que la ligne de depart
                else:
                    #on parcourt la colonne entre la ligne d'arrivee(+1pour pas  
                    #que la tour se voit elle meme) et celle de depart
                    for i in range(caseArrivee.ligne+1,caseDepart.ligne,1):
                        if echiquier.jeu[i][caseArrivee.colonne].piece!=None:
                            return False
            #pas d'obstacle -> retourne true
            return True
                
    ''' On verifie que le Fou peut jouer le coup,
    qu'il n'y a pas d'autre piece sur sa trajectoire
    Si la piece peut, on retourne True et sinon False'''
        
    def verifObstacleFou(self,echiquier,caseDepart,caseArrivee):
        ligneD=caseDepart.ligne
        ligneA=caseArrivee.ligne
        #si le numero de ligne ou de colonne est negatif ou superieur a 8, on
        #est en dehors de l'echiquier -> retourne false
        if ligneA>=8 and caseArrivee.colonne>=8 and ligneA<0 and caseArrivee.colonne<0:
            return False
        #si la colonne d'arrivee ou la ligne est identique a celle de depart
        #on retourne false car ça ne correspond pas a un deplacement en diagonal
        if caseArrivee.colonne-caseDepart.colonne==0 or caseArrivee.ligne-caseDepart.ligne==0:
            return False
        #si la colonne d'arrivee est plus grande a celle de depart
        if caseArrivee.colonne-caseDepart.colonne>0:
            #si la ligne de d'arrivee est plus grande que celle de depart
            if caseArrivee.ligne-caseDepart.ligne>0:
                #on parcourt la diagonale entre la case de depart du fou et celle
                #de son arrivee
                for colonne in range(caseDepart.colonne+1,caseArrivee.colonne,1):
                    ligneD=ligneD+1
                    #si une piece est sur la diagonale -> retourne faux
                    if echiquier.jeu[ligneD][colonne].piece!=None:
                        return False
                    
            #si la ligne de d'arrivee est plus petite que celle de depart    
            if caseArrivee.ligne-caseDepart.ligne<0 :
                #on parcourt la diagonale entre la case de depart du fou et celle
                #de son arrivee
                for colonne in range(caseDepart.colonne+1,caseArrivee.colonne,1):
                        ligneD=ligneD-1
                        #si une piece est sur la diagonale -> retourne faux
                        if echiquier.jeu[ligneD][colonne].piece!=None:
                            return False
        
        #si la colonne d'arrivee est plus petite que celle de depart
        if caseArrivee.colonne-caseDepart.colonne<0:
            #si la ligne d'arrivee est plus grande que celle de depart
            if caseArrivee.ligne-caseDepart.ligne>0:
                #on parcourt la diagonale entre la case de depart du fou et celle
                #de son arrivee 
                for colonne in range(caseArrivee.colonne+1,caseDepart.colonne,1):
                    ligneA=ligneA-1
                    #si une piece est sur la diagonale -> retourne faux
                    if echiquier.jeu[ligneA][colonne].piece!=None:    
                        return False
            
            #si la ligne d'arrivee est plus petite que celle de depart
            if caseArrivee.ligne-caseDepart.ligne<0:
                #on parcourt la diagonale entre la case de depart du fou et celle
                #de son arrivee 
                for colonne in range(caseArrivee.colonne+1,caseDepart.colonne,1):
                    ligneA=ligneA+1
                    #si une piece est sur la diagonale -> retourne faux
                    if echiquier.jeu[ligneA][colonne].piece!=None:
                        return False   
        #si pas d'obstacle -> retourne true
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
        #on sauvegarde dans pieceR le roi
        pieceR=caseR.piece
        #on supprime la piece presente sur case roi
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
                            #si la future case du roi possede une piece
                            if futurCaseRoi.piece!=None:
                                #ennemi est la piece presente sur la future case 
                                #du roi
                                ennemi=futurCaseRoi.piece
                                #on place le roi sur sa future case
                                futurCaseRoi.setPiece(pieceR)
                                #si le pion peut manger le roi
                                if self.pionMangePiece(futurCaseRoi,case,couleur):
                                    #on remet sur la case roi le roi
                                    caseR.setPiece(pieceR)
                                    #on remet sur la case arrivee l'ennemi
                                    futurCaseRoi.setPiece(ennemi)
                                    #on retourne true car le roi est en danger
                                    return True
                                #si le pion ne peut pas manger le roi
                                else:
                                    #on remet sur la case arrivee l'ennemi
                                    futurCaseRoi.setPiece(ennemi)
                            #si la future case du roi comporte une piece
                            else:
                                #si le pion pourra manger le roi sur sa future case
                                #alors le roi est en danger -> return true
                                if self.pionMangePiece(futurCaseRoi,case,couleur):
                                    caseR.setPiece(pieceR)
                                    return True
                        #si c'est une autre piece que le pion
                        else:
                            #si la case d'arrivee du roi comporte une piece
                            if futurCaseRoi.piece!=None:
                                #l'ennemi est la piece presente sur sa case d'arrivee
                                ennemi=futurCaseRoi.piece
                                #on enleve l'ennemi de la case d'arrivee
                                futurCaseRoi.setPiece()
                                #si l'adversaire peut attaquer le roi sur sa 
                                #case d'arrivee
                                if self.adversairePeutAttaquer(case,futurCaseRoi,echiquier):
                                    #on remet l'ennemi sur sa case
                                    futurCaseRoi.setPiece(ennemi)
                                    #on remet le roi sur sa case de depart
                                    caseR.setPiece(pieceR)
                                    #on retourne true car le roi se met en danger
                                    #s'il effactue ce deplacement
                                    return True 
                                
                                #si l'adversaire ne peut pas attaquer le roi
                                #sur sa future case
                                if not self.adversairePeutAttaquer(case,futurCaseRoi,echiquier):
                                    futurCaseRoi.setPiece(ennemi)
                            #si la future case du roi ne comporte pas de piece
                            if futurCaseRoi.piece==None:
                                #si l'adversaire peut attaquer le roi -> retourne
                                #true il est en danger
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
        