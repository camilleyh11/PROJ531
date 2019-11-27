import Pygame #importation du module Pygame

class Pieces: #definition de la classe Pieces 
              #comprend les attributs et les méthodes des pièces d’échecs
    
    def __init__(self): #constructeur qui initialise les variables
        self.initPygame() #initialisation de Pygame
        #initialisation des pièces
        self.pion = pion 
        self.dame = dame
        self.roi = roi
        self.cavalier = cavalier
        self.tour = tour
        self.fou = fou
        
    def piece_echec(self): #méthode pour définir les pièces et leurs attributs
        
        
    #on stocke les images associées aux pièces dans des variables
    #afin de pouvoir les utiliser plustard
    im_tour = fond = pygame.image.load(".jpg")
    im_cavalier = fond = pygame.image.load(".jpg")
    im_fou = fond = pygame.image.load(".jpg")
    im_pion = fond = pygame.image.load(".jpg")
    im_roi = fond = pygame.image.load(".jpg")
    im_dame = fond = pygame.image.load(".jpg")
    
    #on définit le nom des différentes pièces dans la liste piece
    piece=[VIDE,'TOUR','CAVALIER','FOU','PION','ROI','DAME']  
    #on définit les différentes images des pièces dans la liste image
    image=[VIDE,im_tour,im_cavalier, im_fou, im_pion, im_roi, im_dame]
    
    
###############################################################################  
    '''Pour éviter les débordements, on utilise la méthode
    mailbox pour avoir un tableau de 64 et de 120 éléments'''
    
    def tab120 (self):
        tab120 = (
                 -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                 -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                 -1, 0, 1, 2, 3, 4, 5, 6, 7, -1,
                 -1, 8, 9, 10, 11, 12, 13, 14, 15, -1,
                 -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
                 -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
                 -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
                 -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
                 -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
                 -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
                 -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                 -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
                 )
        
        
    def tab64 (self):
        tab64 = (
                 21, 22, 23, 24, 25, 26, 27, 28,
                 31, 32, 33, 34, 35, 36, 37, 38,
                 41, 42, 43, 44, 45, 46, 47, 48,
                 51, 52, 53, 54, 55, 56, 57, 58,
                 61, 62, 63, 64, 65, 66, 67, 68,
                 71, 72, 73, 74, 75, 76, 77, 78,
                 81, 82, 83, 84, 85, 86, 87, 88,
                 91, 92, 93, 94, 95, 96, 97, 98
                 )
###############################################################################



###############################################################################
'''Tour : Déplacement vertical et horizontal. Se déplace tant que la tour n'est 
pas bloquée par une autre pièce'''


    def deplacement_tour(self, position, couleur, echiquier): #méthode pour déplacer la tour
        #deplacement vertical et horizontal
        #On utilise un tuple car il permet une affectation multiple
        deplacements_tour = (-10,10,-1,1) #deplacement vertical et horizontal
        
        future_position_tour = []#on créé une liste vide qui correspond aux déplacements possibles de la tour
        
        #on parcourt les déplacements de la tour, ex: (10, -10, 1, -1)
        for i in deplacements_tour:
            #on "multiplie" les déplacements initiaux pour envisager
            #tous les déplacements possible sur l'échiquier, ex: (20, -20, 2, -2)
            for multiple in range (1,20,1):
                #calcul des nouvelles positions envisageables
                pos_calcul = self.tab120[self.tab64[position] + (multiple*i)]
                #on vérifie que la position calculé ne déborde pas du plateau de jeu
                if pos_calcul != -1:
                    #si la case envisagé est vide et est de couleur identique
                    if (echiquier.cases[pos_calcul].isEmpty() and echiquier.cases[pos_calcul].couleur_case==couleur):
                        #on ajoute cette position à la liste des déplacements 
                        #remarque: on ajoute la position initiale à la liste
                        #car la tour n'est pas obligé de se déplacer
                        future_position_tour.append((position,pos_calcul))
        #on retourne la liste des positions possibles de la tour
        return future_position_tour
###############################################################################              
            
    

###############################################################################        
'''Fou : Déplacement en diagonale. Se déplace tant que le fou n'est pas bloqué 
par une autre pièce.'''   
        

'''Remarque : même raisonnement que pour le déplacement de la tour mais avec
un tuple de déplacement initial différent'''

    def deplacement_fou(self, position, couleur, echiquier):
        deplacements_fou = (-11,-9,11,9)#déplacement en diagonal
        future_position_fou = []
        
        for i in deplacements_tour:
            for multiple in range (1,20,1):
                pos_calcul = self.tab120[self.tab64[position] + (multiple*i)]
                if pos_calcul != -1:
                    if (echiquier.cases[pos_calcul].isEmpty() and echiquier.cases[pos_calcul].couleur_case==couleur):
                        future_position_fou.append((position,pos_calcul))
        return future_position_fou
###############################################################################  
    


###############################################################################    
'''Cavalier : change de couleur à chaque coup, c'est la seule pièce qui peut
passer par dessus une autre pièce, déplacement en "L".'''
      

    def deplacement_cavalier(self, position, couleur, echiquier):
        deplacements_cavalier = (-12,-21,-19,-8,12,21,19,8)#déplacement en "L"
        future_position_cav = []#on créé une liste vide qui correspond aux déplacements possibles du cavalier
        #on parcourt les déplacements du cavalier
        for i in deplacements_cavalier:
            #on calcul les positions possibles en ajoutant -12, -21 etc... 
            #(déplacement en "L") à la position initiale du cavalier
            pos_calcul = self.tab120[self.tab64[position] + i]
            #on vérifie que la position calculé ne déborde pas du plateau de jeu
            if pos_calcul != -1:
                #si la case envisagé est vide et est de couleur opposé
                if (echiquier.cases[pos_calcul].isEmpty() and echiquier.cases[pos_calcul].couleur_case !=couleur):
                    #on ajoute cette position à la liste des déplacements
                    future_position_cav.append((position,pos_calcul))
        #on retourne la liste des positions possibles du cavalier
        return future_position_cav
###############################################################################   
  


###############################################################################     
    def deplacement_dame(self, position, couleur, echiquier):      
############################################################################### 
'''Dame : Se déplace dans toutes les directions, càd comme le cavalier et
le fou à la fois. '''        
        
        
###############################################################################         
    def deplacement_roi(self, position, couleur, echiquier):
############################################################################### 

        

###############################################################################         
    def deplacement_pion(self, position, couleur, echiquier):
############################################################################### 
        
        


