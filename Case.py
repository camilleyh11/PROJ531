# -*- coding: utf-8 -*-
import pygame

class Case:
    def __init__(self) :
        self.couleur=None
        self.piece=None
        self.longeur=50
        self.largeur=50
        self.num=0
    
    def setNum(self,num):
        self.num=num
        
    def setPiece(self, piece):
        self.piece = piece
        
    def setJeu(self,echiquier):
        self.echiquier=echiquier
        
    # Position du premier bouton   
    def getPosition1(self):
        x=(self.echiquier.screen.get_width()//2)-4*self.longeur
        y=(self.echiquier.screen.get_width()//2)-4*self.largeur
        return [x,y]
    
    #Position des autres boutons
#    def getPosition(self):
#        pos1=self.getPosition1()
#        l=self.gConfig.buttonWidth
#        num=self.sensor.sensorId
#        x_boutton=pos1[0]+l*num
#        y_boutton=pos1[1]
#        return[x_boutton,y_boutton]
#        
    #retourne le numero de la ligne du bouton
    def getButtonLines(self):
        num=self.sensor.sensorId
        if num<5:
            return 0
        else:
            return 1
        
    #retourne le numero de la colonne du bouton
    def getButtonColumn(self):
        num=self.sensor.sensorId
        return (num%5)
    
    def drawFirst(self):
        position=self.getPosition1()
        x=position[0]
        y=position[1]
        pygame.draw.rect(self.echiquier.screen, [255,255,255],[x,y,self.largeur,self.longeur], 0)
        
    # Dessine la case
    def draw(self):
        self.drawFirst()
        position=self.getPosition1()
        x=position[0]
        y=position[1]
        num=self.num
        #dessine chaque case
        #Si le numéro de la case est pair alors la case est blanche
        
        
        if num !=0:
            
            if num%8==0:
                num=num+1
                y=y+self.largeur
                x=position[0]
                if num%2==0:
                    pygame.draw.rect(self.echiquier.screen, [255,255,255],[x,y,self.largeur,self.longeur], 0)
                
                    #Si le numéro de la case est impair alors la case est noire
                if num%2==1:
                    pygame.draw.rect(self.echiquier.screen, [0,200,150],[x,y,self.largeur,self.longeur], 0)
    
            if num%8!=0:
                print("coucou")
                x=x+num*self.longeur
                if num%2==0:
                    print("pair")
                    pygame.draw.rect(self.echiquier.screen, [255,255,255],[x,y,self.largeur,self.longeur], 0)
                
                   #Si le numéro de la case est impair alors la case est noire
                if num%2==1:
                    print("impair")
                    pygame.draw.rect(self.echiquier.screen, [0,200,150],[x,y,self.largeur,self.longeur], 0)
     
        
            
        
