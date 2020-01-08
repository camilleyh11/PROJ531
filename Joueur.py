# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:28:31 2020

@author: ruellee
"""

class Joueur:
    def __init__(self, couleur, typejoueur,echiquier,joue):
        self.couleur = couleur  # Blanc ou Noir
        self.typejoueur = typejoueur  # type de joueur: 0 = ordinateur, 1 = humain
        self.echiquier=echiquier
        self.joue=joue
        
    def setJoue(self, jouer):
        self.joue=jouer