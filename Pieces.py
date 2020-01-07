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
#le déplacement du roi 
#principe: peut se déplacer dans les 8 directions possible
#ssi il est pas dans un ROQUE

#ROQUE ?
# -> on déplace le roi de 2 cases vers une de ses tours de manière horizontale
# -> PUIS on déplace la tour en question à l'ancienne place du roi 
       # conditions:
       # -> les cases séparant le roi et la tour sont vides
       # -> on peut roquer 1 seule fois dans la partie 
            #(car tour et roi ne doivent pas avoir bougé avant le roque)
       # -> le roi ne peut pas etre en échec sur son déplacement 
            


#postion = position de départ
#pas_appeler_is_attacked = éviter la récursivité entre is_attacked() et gen_moves_list().    
    def deplacement_roi(self,position,couleur,echiquier,pas_appeler_is_attacked=False):
        
        #on créé une liste vide qui correspond aux déplacements possibles du roi:
        future_position_roi=[]
        
        #pour chaque deplacement du fou et de la tour
        for i in (self.deplacements_tour+self.deplacements_fou):
            n=self.tab120[self.tab64[position]+i]
            if n!=-1:
                if(echiquier.cases[n].isEmpty() or echiquier.cases[n].couleur==echiquier):
                    future_position_roi.append((position,n,''))
    
        #on veut les mouvements possible en mode attack
        if pas_appeler_is_attacked:
                return future_position_roi 
    
        c=echiquier.oppColor(echiquier)
        
    ####            
        # pour le BLANC
        if c=='blanc':
            if echiquier.white_can_castle_63:
             # Si une tour est à la case 63
             # Et si les cases entre le roi et la tour sont vides
             # Et que les cases sur lesquels le ROI se deplacent ne sont pas attaqués
             # Et que le roi n’est pas en mode échec
             # ALORS nous pouvons ajouter ce mouvement de château:
             
                if echiquier.cases[63].nom=='TOUR' and \
                echiquier.cases[63].color=='blanc' and \
                echiquier.cases[61].isEmpty() and \
                echiquier.cases[62].isEmpty() and \
                echiquier.is_attacked(61,'noir')==False and \
                echiquier.is_attacked(62,'noir')==False and \
                echiquier.is_attacked(position,'noir')==False:
                    future_position_roi.append((position,62,''))
                 
         #si une tour est à la case 56   
        if echiquier.white_can_castle_56:        
            if echiquier.cases[56].nom=='TOUR' and \
            echiquier.cases[56].color=='blanc' and \
            echiquier.cases[57].isEmpty() and \
            echiquier.cases[58].isEmpty() and \
            echiquier.cases[59].isEmpty() and \
            echiquier.is_attacked(58,couleur)==False and \
            echiquier.is_attacked(59,couleur)==False and \
            echiquier.is_attacked(position,couleur)==False:
                future_position_roi.append((position,58,''))
                
    ####            
        # pour le NOIR     
        elif c=='noir':
            #si une tour est à la case 7
            if echiquier.black_can_castle_7:
                if echiquier.cases[7].nom=='TOUR' and \
                echiquier.cases[7].color=='noir' and \
                echiquier.cases[5].isEmpty() and \
                echiquier.cases[6].isEmpty() and \
                echiquier.is_attacked(5,couleur)==False and \
                echiquier.is_attacked(6,couleur)==False and \
                echiquier.is_attacked(position,couleur)==False:
                    future_position_roi.append((position,6,''))
                
            #si une tour est à la case 0
            if echiquier.black_can_castle_0:
                 if echiquier.cases[0].nom=='TOUR' and \
                 echiquier.cases[0].color=='noir' and \
                 echiquier.cases[1].isEmpty() and \
                 echiquier.cases[2].isEmpty() and \
                 echiquier.cases[3].isEmpty() and \
                 echiquier.is_attacked(2,couleur)==False and \
                 echiquier.is_attacked(3,couleur)==False and \
                 echiquier.is_attacked(position,couleur)==False:
                     future_position_roi.append((position,2,''))
                
            
            return future_position_roi
    
        

###############################################################################         
'''Le pion se déplace toujours vers l'avant. Il avance d'une ou deux cases, 
ensuite il avance que d'une case. Par contre le pion prend en diagonale.

Arrivé sur la dernière rangée, le pion est obligatoirement promu. Le pion peut 
effectuer une prise en passant.

promotion : pion se transforme -> dame, tour, fou ou cavalier'''

    def deplacement_pion(self, position, couleur, echiquier):

        future_position_pion=[] #on créé une liste vide qui correspond aux déplacements possibles du pion
        
################################## pion blanc #################################
        if couleur=='blanc':
            #Upper square
            #calcul des nouvelles positions envisageables
            pos_calcul=self.tab120[self.tab64[position]-10]
            #on vérifie que la position calculé ne déborde pas du plateau de jeu
            if pos_calcul!=-1:    
                #si la case envisagé est vide
                if echiquier.cases[pos_calcul].isEmpty():
                    #Si le pion est arrivé en position 8 (de 0 à 7)
                    if pos_calcul<8:
                        #il sera promu
                        #on ajoute cette position à la liste des déplacements
                        #remarque: on ajoute la position initiale à la liste
                        #car la tour n'est pas obligé de se déplacer
                        future_position_pion.append((position,pos_calcul,'dame'))                        
                        future_position_pion.append((position,pos_calcul,'tour'))                        
                        future_position_pion.append((position,pos_calcul,'fou'))
                        future_position_pion.append((position,pos_calcul,'cavalier'))  
                        #sinon il avance simplement d'une case et ne fait pas 
                        #de "promotion"
                    else:                        
                        future_position_pion.append((position,pos_calcul,''))
            #Si le pion démarre du début           
            if echiquier.ROW(position)==6:
                #et si les deux cases devant sont vides
                if echiquier.cases[position-8].isEmpty() and echiquier.cases[position-16].isEmpty():
                    #le pion peut avancer de deux cases
                    future_position_pion.append((position,position-16,''))
                    
            ### Capture en haut à gauche ###  
            #calcul des nouvelles positions envisageables
            pos_calcul=self.tab120[self.tab64[position]-11]    
            #on vérifie que la position calculé ne déborde pas du plateau de jeu
            if pos_calcul!=-1:
                #Si la case est de couleur noire
                if echiquier.cases[pos_calcul].couleur=='noir' or echiquier.ep==pos_calcul:
                    #On capture et il sera promu
                    #Si le pion est arrivé en position 8 (de 0 à 7)             
                    if pos_calcul<8                         
                        future_position_pion.append((position,pos_calcul,'dame'))                        
                        future_position_pion.append((position,pos_calcul,'tour'))                        
                        future_position_pion.append((position,pos_calcul,'fou'))                        
                        future_position_pion.append((position,pos_calcul,'cavalier'))                    
                    else:                        
                        future_position_pion.append((position,pos_calcul,''))
                    
            ### Capture en haut à droite ###      
            #raisonnement analogue
            pos_calcul=self.tab120[self.tab64[position]-9]            
            if pos_calcul!=-1:                
                if echiquier.cases[pos_calcul].couleur=='noir' or echiquier.ep==pos_calcul:                    
                    if pos_calcul<8:
                        future_position_pion.append((position,pos_calcul,'dame'))                        
                        future_position_pion.append((position,pos_calcul,'tour'))                        
                        future_position_pion.append((position,pos_calcul,'fou'))                        
                        future_position_pion.append((position,pos_calcul,'cavalier'))                    
                    else:                        
                        future_position_pion.append((position,pos_calcul,'')
                        
                        
                        
################################## pion noir ##################################
                        
        ### Raisonneent analogue au pion blanc ###       
        
        else : 
            pos_calcul=self.tab120[self.tab64[position]+10]
            if pos_calcul!=-1:
                if echiquier.cases[pos_calcul].isEmpty():
                    if pos_calcul>55 :
                        future_position_pion.append((position,pos_calcul,'dame'))                        
                        future_position_pion.append((position,pos_calcul,'tour'))                        
                        future_position_pion.append((position,pos_calcul,'fou'))                        
                        future_position_pion.append((position,pos_calcul,'cavalier'))
                    else :
                        future_position_pion.append((position,pos_calcul,''))
            if echiquier.ROW(position)==1:
                if(echiquier.cases[position+8].isEmpty() and echiquier.cases[position+16].isEmpty()):
                    future_position_pion.append((position,position+16,''))
            pos_calcul=self.tab120[self.tab64[position]+9]
            if pos_calcul!=-1:
                if echiquier.cases[pos_calcul].couleur=='blanc' or echiquier.ep==pos_calcul:
                    if pos_calcul>55:
                        future_position_pion.append((position,pos_calcul,'dame'))                        
                        future_position_pion.append((position,pos_calcul,'tour'))                        
                        future_position_pion.append((position,pos_calcul,'fou'))                        
                        future_position_pion.append((position,pos_calcul,'cavalier'))
                    else : 
                        future_position_pion.append((position,pos_calcul,''))
            pos_calcul=self.tab120[self.tab64[position]+11]
            if pos_calcul!=-1:
                if echiquier.cases[pos_calcul].couleur=='blanc' or echiquier.ep==pos_calcul:
                    if pos_calcul>55:                        
                        future_position_pion.append((position,pos_calcul,'dame'))                        
                        future_position_pion.append((position,pos_calcul,'tour'))                        
                        future_position_pion.append((position,pos_calcul,'fou'))                        
                        future_position_pion.append((position,pos_calcul,'cavalier'))
                    else : 
                        future_position_pion.append((position,pos_calcul,''))
        return future_position_pion        


