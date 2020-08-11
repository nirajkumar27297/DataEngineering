# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:58:11 2020

@author: Niraj
Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N

"""

def harmonicNumber(n):
    if(n == 1):
        return 1
    return 1 / n + harmonicNumber(n - 1)

try:
    n = int(input("Enter the value from which you want to find harmonic number "))
    
    if( n <= 0 ):
        raise Exception
    
    print(round(harmonicNumber(n),2))

except(Exception):
    print("Please enter a positive number")
        
