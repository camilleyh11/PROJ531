# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:35:24 2019

@author: ruellee
"""

import pygame
from Echiquier import Echiquier

def main():
    
    # On cree le jeu d'echec
    echiquier=Echiquier()   
    echiquier.creationJeu()
       
    # Infinite loop
    #tant qu'il n'y a pas de pat ou d'echec et mat la partie continue    
    while not echiquier.moteurJeu.pat and not echiquier.moteurJeu.echecEtMat(echiquier) and not echiquier.moteurJeu.coupAleatoire(echiquier):
         
        # on attend un evenement           
        event = pygame.event.wait()
 
        #Si on clique sur la croix en haut à droite ou qu'on appuie sur echap on ferme le jeu
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            break
        
        elif event.type == pygame.USEREVENT:
            echiquier.display()
                            
        #Quand on appuie sur le clique gauche de la souris, la position est envoyee dans la classe echiquier
        elif event.type == pygame.MOUSEBUTTONDOWN:
            echiquier.mouseButtonDown(event.pos)

        elif event.type== pygame.MOUSEBUTTONUP:
            echiquier.mouseButtonUp(event.pos)
            
        elif event.type== pygame.MOUSEMOTION:
            echiquier.mouseMotion(event.pos)
            
    #on quitte pygame s'il y a pat ou echec et mat
    if echiquier.moteurJeu.echecPat(echiquier):
        print("===============================\n \t PAT EGALITE \n===============================")
    if echiquier.moteurJeu.echecEtMat(echiquier):
        print("=============================== \n \t Les ",echiquier.moteurJeu.getJoueurAdverse().couleur," ont gagné ! \n ===============================")
    print("===============================\n\tFin du jeu\n===============================")
    pygame.quit()
                
# Calls the main function
if __name__ == "__main__":
    main() 
