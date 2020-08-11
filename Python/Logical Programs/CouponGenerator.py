# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:33:40 2020

@author: Niraj Kumar
 Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process
"""

import random

N = int(input("How Many Coupons You Want To Generate : "))
cplen = int(input("Enter Coupon Length : "))
print("Generated Coupon Numbers :")
countCoupons = 0
countRandom = 0
cpnum = ''
couponlist = []
while countCoupons < N:
    cpnum = ''
    for i in range(cplen):
        cpnum += str(random.randint(0, 9))
        countRandom += 1
    if couponlist.count(cpnum) == 0:
        couponlist.append(cpnum)
        countCoupons += 1
for i in range(len(couponlist)):
     print(i+1," : ",couponlist[i])
     
print("The total random number generated for coupons generation is",countRandom)
            
