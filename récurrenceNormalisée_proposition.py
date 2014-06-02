#-*-coding: utf8 -*-
from turtle import *
import math
import sys

from triangle_suite import*

def récurrenceNormalisée(t,red,green,blue, x):

    while True :
        color("brown", [red, green, blue])
        
        tprime = sym(t)
        tpprime = normalize( tprime )
        if DÉBOGUE :
            anglest = sorted(t.minmaxAngles())
            anglestpp = sorted(tpprime.minmaxAngles())
        if not DÉBOGUE :
            anglest = sorted(t.angles())
            anglestpp = sorted(tpprime.angles())
        print(anglestpp)
        if abs(anglestpp[0] - anglest[0]) < TOLÉRANCE and \
            abs(anglestpp[1] - anglest[1]) < TOLÉRANCE and \
            abs(anglestpp[2] - anglest[2]) < TOLÉRANCE :
            print( "\n¡ Convergence !\n sur angles :", tpprime.angles(),
                      "\nTriangle final :", tpprime,
                      "\nTriangle précédent:", t,
                      "\navec angles :", t.angles())
            print("\nTolérance =",TOLÉRANCE)
            sys.exit() # à faire plus joli
        begin_fill()
        tpprime.dessin()
        end_fill()
  
        if x < 20:
            red += 7
            green += 7
            blue += 7
        else:
            red += 1
            green += 1
            blue += 1


        x += 1

        #print(red, green, blue)

        if red < 0:
            red = 0
        elif red > 255:
            red = 255
        if green < 0:
            green = 0
        elif green > 255:
            green = 255
        if blue < 0:
            blue = 0
        elif blue > 255:
            blue = 255

        récurrenceNormalisée( tpprime, red, green, blue, x )

colormode(255)
speed(10)

RR = 0
GG = 0
BB = 0
x = 0

# récurrenceNormalisée(T, RR, GG, BB, x) pour lancer le programme !
