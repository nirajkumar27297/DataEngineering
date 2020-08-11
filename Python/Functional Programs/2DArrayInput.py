# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:32:30 2020

@author: Niraj
A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
"""
#Taking input through command line argument
nrows,ncols = [int(x) for x in input("Enter the number of rows and columns ").split()]

#Taking input for array
arr = []
for i in range(nrows):
    print("Enter row ",i," values separated by space")
    #Taking input through command line argument
    value = [int(x) for x in input().split()]
    arr.append(value)

#Printing arr
for i in range(nrows):
    for j in range(ncols):
        print(arr[i][j],end= " ")
    print()
    
                                                
