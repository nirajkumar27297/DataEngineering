# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 00:21:54 2020

@author: hp
Find all the triplets whose sum is zero
"""

def triplets(arr):
    #Sorting the array
    arr.sort()
    countTriplets = 0
    print("The triplets are")
    for i in range(0,len(arr)-2):
        startIndex = i + 1
        endIndex = len(arr) -1
        while(startIndex < endIndex):
            if(arr[startIndex] + arr[endIndex] > -arr[i]):
                endIndex -= 1
            elif(arr[startIndex] + arr[endIndex] < -arr[i]):
                startIndex += 1
            else:
                print(arr[i],arr[startIndex],arr[endIndex])
                countTriplets += 1
                startIndex += 1
                endIndex -= 1
    
    print("The total number of triplets are ",countTriplets)

# Size of triplets
n = input("Enter the size of the array")
#input array
arr = [int(x) for x in input("Enter the elements of the array ").split()]
        
        