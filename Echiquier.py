# -*- coding: utf-8 -*-
import pygame
from Case import Case
from Piece import Piece
from Jeu import Jeu
from Joueur import Joueur
#from deplacement_des_pieces import Pieces

class Echiquier:
    
    # Constructeur
    def __init__(self) :
        self.MoteurJeu=Jeu()
        self.joueur=Joueur('Blanc',1,self,True)
        self.ordi=Joueur('Noir',0,self,False)
        self.initPygame()
        self.jeu=[]
        self.caseLongueur=75
        self.caseLargeur=75
        self.coupValide=False
        self.caseDepart=None
        self.caseArrivee=None
        self.deplacement=None

        # chargement d'une image contenant toutes les pieces
        # et redimensionnement à la taille des cases
        self.imagesPieces=pygame.image.load("2000px-Chess_Pieces_Sprite.png")
        self.imagesPieces = pygame.transform.scale(self.imagesPieces,
                                                   (self.caseLongueur*6,
                                                    self.caseLargeur*2))
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
            tabLigne=[]
            # j represente les colonnes
            for colonne in range(8): 
        
                # On calcule la position de la case en fonction de la premiere
        
                x=position[0]+colonne*self.caseLongueur
                y=position[1]+ligne*self.caseLargeur
                
                #on recupere la couleur
                couleur=self.caseCouleur(ligne,colonne)
            
                tabLigne.append(Case(ligne,colonne,couleur,[x,y,self.caseLongueur,self.caseLargeur]))
            self.jeu.append(tabLigne)
                
        self.creationPieces()
                
        
    def creationPieces(self):

        #creation des pieces blanches
        
        #creation Roi Blanc
        roiBlanc=Piece('Blanc','Roi',(0*self.caseLongueur,0*self.caseLargeur,
                                    self.caseLongueur,self.caseLargeur))
        self.jeu[7][4].setPiece(roiBlanc)
       
        #creation Reine Blanc
        reineBlanc=Piece('Blanc','Reine',(1*self.caseLongueur,0*self.caseLargeur,
                                    self.caseLongueur,self.caseLargeur))
        self.jeu[7][3].setPiece(reineBlanc)
        
        #creation Fou Blanc
        for i in [2,5]:
            fouBlanc=Piece('Blanc','Fou',(2*self.caseLongueur,0*self.caseLargeur,
                                        self.caseLongueur,self.caseLargeur))
            self.jeu[7][i].setPiece(fouBlanc)
        
        #creation Cavalier Blanc
        for i in [1,6]:
            cavalierBlanc=Piece('Blanc','Cavalier',(3*self.caseLongueur,0*self.caseLargeur,
                                        self.caseLongueur,self.caseLargeur))
            self.jeu[7][i].setPiece(cavalierBlanc)
        
        #creation Pion Blanc
        for i in range(0,8):
            pionBlanc=Piece('Blanc','Pion',(5*self.caseLongueur,0*self.caseLargeur,
                                        self.caseLongueur,self.caseLargeur),i,False)
            
            self.jeu[6][i].setPiece(pionBlanc)
            
        #creation Tour Blanc
        for i in [0,7]:
            tourBlanc=Piece('Blanc','Tour',(4*self.caseLongueur,0*self.caseLargeur,
                                        self.caseLongueur,self.caseLargeur))
            self.jeu[7][i].setPiece(tourBlanc)
            
            
        
        #creation des pieces noires
        
        #creation Roi Noir
        roiNoir=Piece('Noir','Roi',(0*self.caseLongueur,1*self.caseLargeur,
                                    self.caseLongueur,self.caseLargeur))
        self.jeu[0][4].setPiece(roiNoir)
        
        #creation Reine Noir
        reineNoir=Piece('Noir','Reine',(1*self.caseLongueur,1*self.caseLargeur,
                                    self.caseLongueur,self.caseLargeur))
        self.jeu[0][3].setPiece(reineNoir)
        
        #creation Fou Noir
        for i in [2,5]:
            fouNoir=Piece('Noir','Fou',(2*self.caseLongueur,1*self.caseLargeur,
                                        self.caseLongueur,self.caseLargeur))
            self.jeu[0][i].setPiece(fouNoir)
        
        #creation Cavalier Noir
        for i in [1,6]:
            cavalierNoir=Piece('Noir','Cavalier',(3*self.caseLongueur,1*self.caseLargeur,
                                        self.caseLongueur,self.caseLargeur))
            self.jeu[0][i].setPiece(cavalierNoir)
        
        #creation Pion Noir
        for i in range(0,8):  
            pionNoir=Piece('Noir','Pion',(5*self.caseLongueur,1*self.caseLargeur,
                                        self.caseLongueur,self.caseLargeur),i,False)
            
            self.jeu[1][i].setPiece(pionNoir)
            
        #creation Tour Noir
        for i in [0,7]:
            tourNoir=Piece('Noir','Tour',(4*self.caseLongueur,1*self.caseLargeur,
                                        self.caseLongueur,self.caseLargeur))
            self.jeu[0][i].setPiece(tourNoir)
        
        
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
        self.joue()
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
                    
    def joue(self):
                if self.joueur.joue:
                    if self.caseDepart != None:
                        if self.caseDepart.piece.couleur==self.joueur.couleur:
                                self.deplacementPiece()
                                if self.coupValide:
                                    self.joueur.setJoue(False)
                                    self.ordi.setJoue(True)
                                    self.coupValide=False
                else:
                    if self.caseDepart != None:
                        if self.caseDepart.piece.couleur==self.ordi.couleur:
                                self.deplacementPiece()
                                if self.coupValide:
                                    self.ordi.setJoue(False)
                                    self.joueur.setJoue(True)
                                    self.coupValide=False
    #def miseDangerRoi(self):
        
        
    def deplacementPiece(self):
        
        if self.caseDepart!=None and self.caseDepart.piece!=None:
            pieceD= self.caseDepart.piece
            if self.caseArrivee!=None and (self.caseArrivee.piece== None or self.caseArrivee.piece.couleur!=pieceD.couleur)and self.verifObstacle(pieceD.nom):
                if pieceD.nom=='Tour':
                    if self.MoteurJeu.deplacement_tour(self.caseArrivee,self.caseDepart):
                        self.coupValide=True
                        self.caseDepart.setPiece()
                        self.caseArrivee.setPiece(pieceD)
                if pieceD.nom=='Fou':
                    if self.MoteurJeu.deplacement_fou(self.caseArrivee,self.caseDepart):
                        self.coupValide=True
                        self.caseDepart.setPiece()
                        self.caseArrivee.setPiece(pieceD)
                if pieceD.nom=='Reine':
                    if self.MoteurJeu.deplacement_reine(self.caseArrivee,self.caseDepart):
                        self.coupValide=True
                        self.caseDepart.setPiece()
                        self.caseArrivee.setPiece(pieceD)
                        
                if pieceD.nom=='Roi':
                    if self.MoteurJeu.deplacement_roi(self.caseArrivee,self.caseDepart):
                        self.coupValide=True
                        self.caseDepart.setPiece()
                        self.caseArrivee.setPiece(pieceD)
                        
                if pieceD.nom=='Cavalier':
                    if self.MoteurJeu.deplacement_cavalier(self.caseArrivee,self.caseDepart):
                        self.coupValide=True
                        self.caseDepart.setPiece()
                        self.caseArrivee.setPiece(pieceD)
                        
                if pieceD.nom =='Pion' and self.verifObstacle(pieceD.nom,pieceD.couleur) :
                    if self.MoteurJeu.deplacement_pion(self.caseArrivee,self.caseDepart,self.caseDepart.piece.couleur):
                        self.coupValide=True
                        self.caseDepart.setPiece()
                        self.caseArrivee.setPiece(pieceD)
            
            
    def verifObstacle(self,nom,couleur=None):
        if nom=='Tour':
            return self.verifObstacleTour()
        if nom=='Fou':
            return self.verifObstacleFou()
        if nom=='Reine' or nom=='Roi':
            if self.caseArrivee.ligne==self.caseDepart.ligne or self.caseArrivee.colonne==self.caseDepart.colonne:
                return self.verifObstacleTour()
            else:
                return self.verifObstacleFou()
        if nom=='Pion' and couleur=='Blanc': 
            if self.caseArrivee.colonne==self.caseDepart.colonne:
                for i in range(self.caseArrivee.ligne,self.caseDepart.ligne,1):
                    if self.jeu[i][self.caseDepart.colonne].piece!=None:
                                return False
        if nom=='Pion' and couleur=='Noir': 
            if self.caseArrivee.colonne==self.caseDepart.colonne:
                for i in range(self.caseDepart.ligne+1,self.caseArrivee.ligne+1,1):
                    if self.jeu[i][self.caseDepart.colonne].piece!=None:
                                return False
        return True
                
                
        
        
    def verifObstacleTour(self):
            if self.caseArrivee.ligne==self.caseDepart.ligne:
                if self.caseArrivee.colonne-self.caseDepart.colonne>0:
                    for i in range(self.caseDepart.colonne+1,self.caseArrivee.colonne,1):
                        if self.jeu[self.caseArrivee.ligne][i].piece!=None:
                            return False
                else:
                    for i in range(self.caseArrivee.colonne+1,self.caseDepart.colonne,1):
                        if self.jeu[self.caseArrivee.ligne][i].piece!=None:
                            return False
                        
                        
            if self.caseArrivee.colonne==self.caseDepart.colonne:
                
                if self.caseArrivee.ligne-self.caseDepart.ligne>0:
                    for i in range(self.caseDepart.ligne+1,self.caseArrivee.ligne,1):
                        if self.jeu[i][self.caseArrivee.colonne].piece!=None:
                            return False
                else:
                    for i in range(self.caseArrivee.ligne+1,self.caseDepart.ligne,1):
                        if self.jeu[i][self.caseArrivee.colonne].piece!=None:
                            return False
            return True
                        
    def verifObstacleFou(self):
            if self.caseArrivee.colonne-self.caseDepart.colonne>0:
                if self.caseArrivee.ligne-self.caseDepart.ligne>0:
                    for i in range(self.caseDepart.colonne+1,self.caseArrivee.colonne,1):
                        for j in range(self.caseDepart.ligne+1,self.caseArrivee.ligne,1):
                            if self.jeu[j][i].piece!=None:
                                return False
                else:
                    for i in range(self.caseDepart.colonne+1,self.caseArrivee.colonne,1):
                        for j in range(self.caseArrivee.ligne+1,self.caseDepart.ligne,1):
                            if self.jeu[j][i].piece!=None:
                                return False
            else:
                if self.caseArrivee.ligne-self.caseDepart.ligne>0:
                    for i in range(self.caseArrivee.colonne+1,self.caseDepart.colonne,1):
                        for j in range(self.caseDepart.ligne+1,self.caseArrivee.ligne,1):
                            if self.jeu[j][i].piece!=None:
                                return False
                else:
                    for i in range(self.caseArrivee.colonne+1,self.caseDepart.colonne,1):
                        for j in range(self.caseArrivee.ligne+1,self.caseDepart.ligne,1):
                            if self.jeu[j][i].piece!=None:
                                return False          
            return True
            
        
    
    
    
            
    # Permet d'afficher les cases de l'echiquier
    def display(self):
        #efface l'ecran en noir
        pygame.draw.rect(self.screen,[0,0,0],[0,0,self.screen.get_width(),self.screen.get_height()],0)
                    
        # dessine l'echiquier
        for ligne in self.jeu:
            for case in ligne:
                self.drawCase(case) 
                
        if self.caseDepart!=None:
            if self.caseDepart.piece!=None and (self.caseDepart.piece.rect != None) :
                    
#            img = pygame.image.load("45px-Chess_kdt45.png")
#            img = pygame.transform.scale(img, (75, 75))
#            self.screen.blit(img, (self.deplacement[0]-75//2,self.deplacement[1]-75//2))
                    self.screen.blit(self.imagesPieces,
                                     (self.deplacement[0]-75//2,
                                      self.deplacement[1]-75//2),
                                      self.caseDepart.piece.rect)
            
#            surface=pygame.Surface((333,333))
#            img.blit(surface, (self.deplacement[0]-333//2,self.deplacement[1]-333//2),(0,0,600,600))         
#            img = pygame.transform.scale(surface,(250,250))
#            self.screen.blit(img, (self.deplacement[0]-600//2,self.deplacement[1]-100//2))
            
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
                
    
    #dessine les cases de l'echiquier
    def drawCase(self,case):
        
        pygame.draw.rect(self.screen, case.couleur,case.rect, 0)
        
        if case.piece!=None:
            self.screen.blit(self.imagesPieces,
                             (case.rect[0],case.rect[1]),
                              case.piece.rect)
                
