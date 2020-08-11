# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:47:16 2020

@author: Niraj Kumar
 This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N
"""

try:
    n = int(input("Enter the value upto which you want to print power table "))
    if(n < 0 or n >= 31 ):
        raise Exception
    
    i = 0
    print("The power table is")
    while(1):
        product = 2 ** i
        print("2 ^ ",i," = ",product)
        if(product >= 2**n ):
            break
        i += 1

except(Exception):
    print("Please enter the number in range 0 and 31")
    

