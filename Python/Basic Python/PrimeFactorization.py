# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:11:49 2020

@author: Number
Prime Factorixation of the number
"""
import math

n = int(input("Enter the number from which u need to find prime factors "))
#Dividing the number by 2 and getting all the factors of 2
while n % 2 == 0:
    print(2,end = " ")
    n = n // 2

#By this time n is odd so skip of 2 

for i in range(3,int(math.sqrt(n)) + 1,2):
    #while i divides n print i and divide n by i
    while n % i == 0:
        print(i,end = " ")
        n = n // i

#if n is prime then number should be greater than 2
if n > 2:
    print(n)

