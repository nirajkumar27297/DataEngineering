# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:43:20 2020

@author: Niraj Kumar
Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). 
"""
import math
x,y = [int(x) for x in input("Enter X and Y coordinates ").split()]
#calculating Euclidean Distance
distanceBetweenPoints = math.sqrt(math.pow(x,2) + math.pow(y,2))
print("The distance of the points from the origin is ",round(distanceBetweenPoints,2)) 

