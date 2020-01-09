# -*- coding: utf-8 -*-
import pygame
from Case import Case
from Piece import Piece
from Jeu import Jeu
#from Joueur import Joueur
#from deplacement_des_pieces import Pieces

class Echiquier:
    
    # Constructeur
    def __init__(self) :
        self.moteurJeu=Jeu()
        self.initPygame() # initialisation de pygame
        self.jeu=[] # plateau de jeu qui va contenir les cases de l'echiquier
        self.caseLongueur=75
        self.caseLargeur=75
        #self.coupValide=False # Pour savoir si le coup joue est valide
        self.caseDepart=None # Case correspondant premier click de la souris
        self.caseArrivee=None # Là ou l'utilisateur relache le click de la souris
        self.deplacement=None # coordonnees [x,y] du curseur du deplacement de la souris

        # chargement d'une image contenant toutes les pieces
        # et redimensionnement à la taille des cases :
        # il y a 6 pieces sur l'image qui doivent donc tenir sur 6 cases, il y
        # a deux rangees de pieces qui doivent donc tenir sur 2 lignes,
        # la longueur et largeur d'une case = 75 donc la nouvelle taille de 
        # l'image doit etre de 6*75 sur 2*75
        self.imagesPieces=pygame.image.load("2000px-Chess_Pieces_Sprite.png")
        self.imagesPieces = pygame.transform.scale(self.imagesPieces,
                                                   (self.caseLongueur*6,
                                                    self.caseLargeur*2))
        
        
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
        
###############################################################################
        ''' GETTERS'''
###############################################################################
        
    ''' Position de la premiere case, on recupere la taille de l'ecran de jeu 
     que l'on divise par 2. On a donc la moitie de l'ecran. 
     On enleve ensuite 4 cases à cette valeur (en x et en y) pour avoir 
     x1 et y1 de la premiere case''' 
    
    def getPositionCase1(self):
        x=(self.screen.get_width()//2)-4*self.caseLongueur
        y=(self.screen.get_height()//2)-4*self.caseLargeur
        return [x,y]
        
    ''' Retourne la couleur de la case correspondante à la ligne et la colonne
    passees en parametre'''
    
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
            
    '''Renvoie la case correspondant à la position en pixel ou renvoie null si
    les coordonnées sont hors du plateau de jeu'''
    
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
    
    def getCaseRoi(self,couleur):
        for ligne in self.jeu:
            for case in ligne:
                if case.piece != None:                    
                    if case.piece.couleur==couleur and case.piece.nom=='Roi':
                        return [case.ligne,case.colonne]
    
###############################################################################
    '''INITIALISATION DU PLATEAU DE JEU'''
###############################################################################
    
    ''' On cree une matrice de 64 case de 8 lignes et 8 colonnes'''
    
    def creationJeu(self):
        # On recupere la position de la premiere case
        position=self.getPositionCase1()
        
        # On parcourt les 8 lignes 
        for ligne in range(8):
            tabLigne=[]
            # on parcourt les colonnes
            for colonne in range(8): 
        
                # On calcule la position de la case en fonction de la premiere
        
                x=position[0]+colonne*self.caseLongueur
                y=position[1]+ligne*self.caseLargeur
                
                # On recupere la couleur de la case
                couleur=self.caseCouleur(ligne,colonne)
                
                # On ajoute la case dans une liste qui represente la ligne
                tabLigne.append(Case(ligne,colonne,couleur,[x,y,self.caseLongueur,self.caseLargeur]))
            # On ajoute une ligne dans le tableau 
            self.jeu.append(tabLigne)
        # On cree les pieces
        self.creationPieces()
                
    ''' Creation des pieces'''
    
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
        
   
###############################################################################          
    ''' DIFFERENTES ACTIONS DE LA SOURIS'''
###############################################################################
                                
    # Quand on appuie sur la souris
    def mouseButtonDown(self,coord):
        # On sauvegarde la case de depart et 
        # on initialise le deplacement à cette coordonees
        self.caseDepart=self.getCase(coord)
        self.deplacement=coord
        

    # Quand on relache la souris
    def mouseButtonUp(self,coord):
        # On sauvegarde la case d'arrivee, on appelle joue
        # et on efface la valeur de caseDepart
        self.caseArrivee=self.getCase(coord)
        self.moteurJeu.joue(self.caseDepart,self.caseArrivee,self)
        self.caseDepart=None
        

    # Quand on deplace la souris
    def mouseMotion(self,coord):
        self.deplacement=coord
        
    
###############################################################################
    '''AFFICHAGE'''        
###############################################################################
    
            
    ''' Permet d'afficher l'echiquier'''
    def display(self):
        # efface l'ecran en noir pour ne pas voir les pieces qui sortent
        # du plateau de jeu
        pygame.draw.rect(self.screen,[0,0,0],[0,0,self.screen.get_width(),self.screen.get_height()],0)
                    
        # dessine l'echiquier
        for ligne in self.jeu:
            for case in ligne:
                self.drawCase(case) 
        
        # Si un deplacement a ete initialise
        if self.caseDepart!=None:
            if self.caseDepart.piece!=None and (self.caseDepart.piece.rect != None) :
                    
                    # on prend d'abord l'image de toute les pieces et nous prenons
                    # le rectangle de cette image correspondant à l'image de la piece
                    # on enleve la moitie de la case pour que l'image soit centrée 
                    # sur le curseur
                    self.screen.blit(self.imagesPieces,
                                     (self.deplacement[0]-75//2,
                                      self.deplacement[1]-75//2),
                                      self.caseDepart.piece.rect)       
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
                
    '''dessine la cases passee en parametre'''

    def drawCase(self,case):
        
        pygame.draw.rect(self.screen, case.couleur,case.rect, 0)
        
        if case.piece!=None:
            #Si la case possede une piece, on la dessine
            self.screen.blit(self.imagesPieces,
                             (case.rect[0],case.rect[1]),
                              case.piece.rect)
            
###############################################################################               
###############################################################################