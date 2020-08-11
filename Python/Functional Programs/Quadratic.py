# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:49:20 2020

@author: Niraj Kumar
find the roots of the equation a*x*x + b*x + c
"""
import math
a,b,c = [int(x) for x in input("Enter the value of a,b,c for equation a*x*x + b*x + c ").split()]
#calculating discriminant
discriminant = b*b - 4 * a * c
if( discriminant > 0 ):
    firstRoot = round(( -b + math.sqrt(discriminant)) / (2 * a),2)
    secondRoot = round(( -b - math.sqrt(discriminant)) / (2 * a),2)
    
    print("The roots of the equation are real ",firstRoot,secondRoot)
elif( discriminant == 0 ):
    firstRoot = round(( -b / (2 * a)),2)
    print("The roots of the equations are real and equal ",firstRoot,firstRoot)
else:
    print("The roots are imaginery")
    

