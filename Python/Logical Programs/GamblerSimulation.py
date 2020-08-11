# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:31:19 2020

@author: Niraj Kumar
Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goa
"""
import random
stakeAmount = int(input('Enter the stake amount '))
betAmount = int(input('Enter the bet amount '))
goalAmount = int(input('Enter the goal amount '))
countWin = 0
countLost = 0
#Starting game
while(1):
    """"
    0 - lost bet amount
    1 - gain bet amount
    """
    bet = random.randint(0,1)
    if( bet == 0 ):
        print("Oops !!! You lost")
        stakeAmount -= betAmount
        countLost += 1
    else:
        print("Congrats!!!! You Won ")
        stakeAmount += betAmount
        countWin += 1
    print("You stake amount is ",stakeAmount)
    
    if(stakeAmount == goalAmount):
        print("You have reached your goal amount")
        break;
    elif(stakeAmount <= 0 ):
        print("You have lost your whole money...Game Stops")
        break;

percentageWin = (countWin / (countWin + countLost)) * 100
percentageLose = (countLost / (countWin + countLost)) * 100
print("The winning percentage is ",round(percentageWin,2))
print("The losing percentage is ",round(percentageLose,2))
        
    
    
    
    


