# -*- coding: utf-8 -*-

import math
import random
import pygame
# frame per second
fr =60.0


def dice(p1,p2):
# the distance between two points
    return math.ceil(math.sqrt( abs((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )))
# color
yellow =(255,255,0)
blue =(0,0,255)
black =(0,0,0)

# the class

class Point:

    def __init__(self,color,x=random.randrange(100,400) ,y=random.randrange(100,400),angle=random.randrange(0,360),speed= 90,r =3,alive=True,key_r= pygame.K_RIGHT,key_l=pygame.K_LEFT):
        self.__color= color
        self.__current_position= [random.randrange(100,400),random.randrange(100,400)]
        self.__angel= angle
        self.__speed= speed
        self.__r = r
# check if the character is a live
        self.__alive = alive
   
        self.__trail = []
 
        self.__imaginary_trail=[]
    # Is the character jumping 
        self.__painting=False

        self.__key_r =key_r
        self.__key_l =key_l
     #   Because it works with pixels, and you cannot define half a pixel, I store the extra pixels in these parameters.
        self.__xe =0.0
        self.__ye =0.0
# Timer of elapsed time from the last jump 
        self.__jumpcounter =60


    def update_position(self):
# update the position of the character 

        self.__current_position= [self.__current_position[0]+math.modf(((self.__speed/fr)*math.cos(math.radians(90-self.__angel))))[1],self.__current_position[1]+math.modf(((self.__speed/fr)*math.cos(math.radians(180+self.__angel))))[1]]

        self.__xe +=math.modf(((self.__speed/fr)*math.cos(math.radians(90-self.__angel))))[0]
        self.__ye +=math.modf(((self.__speed/fr)*math.cos(math.radians(180+self.__angel))))[0]

        self.__current_position=[int(math.modf(self.__xe)[1]+self.__current_position[0]),int(math.modf(self.__ye)[1]+self.__current_position[1])]

        self.__xe =math.modf(self.__xe)[0]
        self.__ye =math.modf(self.__ye)[0]

    def return_position(self):

        return self.__current_position
    def move_right(self):
    # move right
        self.__angel+=2
        self.__angel = abs(self.__angel%360)
    def move_left(self):
    # move left
        self.__angel-=2
        self.__angel = abs(self.__angel%360)
    def power_up(self):

        pass


    def ubdite_trail(self):
# send the location of the character
        i =int( self.__r/(self.__speed/float(fr))+3)
        if len(self.__imaginary_trail) < i:
            self.__imaginary_trail =  self.__imaginary_trail +[self.__current_position]

        else:

            self.__trail = self.__imaginary_trail[:len(self.__imaginary_trail)-i+1:]


            self.__imaginary_trail = self.__imaginary_trail[len(self.__imaginary_trail)-i::]+ [self.__current_position]

        return self.__trail


    def check_collision(self,all_trilse):
# no collision

        if all_trilse[self.__current_position[0]][self.__current_position[1]] == True :
            self.__alive=False

    def play(self,all_tilse,screen):
 # the character movement in one frame

        if not self.__alive:
            print "dead"
            return "dead"
        if self.__painting:
 
            pygame.draw.circle(screen,self.__color, self.__current_position, self.__r)

            self.update_position()

            self.check_collision(all_tilse)

            pygame.draw.circle(screen,yellow, self.__current_position, self.__r)
            if self.__jumpcounter ==0:
                self.__painting=False
                self.__jumpcounter =30
            self.__jumpcounter -=1
            return self.ubdite_trail()
        else:
# when a character is jumping
            pygame.draw.circle(screen,black, self.__current_position, self.__r)
            self.update_position()
            pygame.draw.circle(screen,yellow, self.__current_position, self.__r)
            if self.__jumpcounter ==0:
                self.__painting=True
                self.__jumpcounter =random.randrange(3,7,1)*fr
            self.__jumpcounter -=1
            return "jumping"





    """
    def __str__(self):
        return "x= "+str( self.__x) +", y= "+ str(self.__y)
    def __repr__(self):
        return  "x= "+str( self.__x) +", y= "+ str(self.__y)
    """