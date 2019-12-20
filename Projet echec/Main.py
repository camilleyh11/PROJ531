# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:35:24 2019

@author: ruellee
"""

import pygame
from Echiquier import Echiquier
from Piece import Piece


def main():
    jeu=Echiquier()
    jeu.creationJeu()
    
    
    
    # Infinite loop    
    while True:

        # Waits for an event
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Displays the selected sensor
        elif event.type == pygame.USEREVENT: 
            jeu.display()
                                  
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            # Checks if the display of a new sensor is required
#            jeu.checkIfSensorChanged(event.pos)
                
# Calls the main function
if __name__ == "__main__":
    main() 