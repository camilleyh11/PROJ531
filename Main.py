# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:35:24 2019

@author: ruellee
"""

import pygame
from Echiquier import Echiquier

def main():
    jeu=Echiquier()  
    
    jeu.creationJeu()
       
    # Infinite loop
    #tant qu'il n'y a pas de pat ou d'echec et mat la partie continue    
    while not jeu.moteurJeu.pat and not jeu.moteurJeu.echecEtMat(jeu):
        # Waits for an event
            
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            break
        
        elif event.type == pygame.USEREVENT:
            jeu.display()
                                  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            jeu.mouseButtonDown(event.pos)

        elif event.type== pygame.MOUSEBUTTONUP:
            jeu.mouseButtonUp(event.pos)
            
        elif event.type== pygame.MOUSEMOTION:
            jeu.mouseMotion(event.pos)
    #on quitte pygame s'il y a pat ou echec et mat
    print('Fin du jeu')
    pygame.quit()
                
# Calls the main function
if __name__ == "__main__":
    main() 
