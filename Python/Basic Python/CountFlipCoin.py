# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:29:38 2020

@author: Niraj
Count Percentage of Heads and Tails
"""
import random 

try:
    numberOfFlips = int(input("Enter the number of times you want to flip the coin "))
    if( numberOfFlips < 0 ):
        raise Exception
    #Total count
    totalCount = 0
    countHead = 0
    while( totalCount < numberOfFlips ):
        flip = random.random()
        if ( flip > 0.5 ):
            countHead += 1
        totalCount += 1
    headPercentage = (countHead / totalCount) * 100
    print("Percentage of Head is {0:.2f}".format(headPercentage))
    tailPercentage = ((totalCount - countHead) / totalCount) * 100
    print("Percentage of Tail is {0:.2f}".format(tailPercentage))

except(Exception):
    print("Enter a positive number")
    
    


