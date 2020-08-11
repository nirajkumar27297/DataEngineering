# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 00:45:43 2020

@author: Niraj Kumar
Initialize deck of cards having suit ("Clubs",
"Diamonds", "Hearts", "Spades") & Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10",
"Jack", "Queen", "King", "Ace"). Shuffle the cards using Random method and then
distribute 9 Cards to 4 Players and Print the Cards the received by the 4 Players
using 2D Array
"""
import random

class DeckOfCards:
    def __init__(self):
        self.cardDistribution = [[ 0 for j in range(13)] for i in range(4)]
        self.cardsDict ={}
        for i in range(4):
            cardList = [ i+1 for i in range(13)]
            self.cardsDict[i]= cardList
    
    def generateCard(self):
        while(1):
            cardType = random.randint(0,3)
            if(len(self.cardsDict[cardType]) == 0):
                continue
            cardNumber = random.choice(self.cardsDict[cardType])
            self.cardsDict[cardType].remove(cardNumber)
            
            if(cardType == 0):
                cardType = "Heart"
            elif(cardType == 1):
                cardType = "Spade"
            elif(cardType == 2):
                cardType = "Club"
            elif(cardType == 3):
                cardType = "Diamond"
            
            if(cardNumber == 1):
                cardNumber = "ACE"
            elif(cardNumber == 11):
                cardNumber = "King"
            elif(cardNumber == 12):
                cardNumber = "Queen"
            elif(cardNumber == 13):
                cardNumber = "Jack"
            else:
                cardNumber = str(cardNumber)
            return cardType+" "+cardNumber
    
    def distributeCards(self):
        for i in range(4):
            for j in range(13):
                self.cardDistribution[i][j] = self.generateCard()
    
    def printcards(self):
        for i in range(4):
            print("Player ",i+1)
            for j in range(13):
                print(  self.cardDistribution[i][j])
            print("*************************************")
objDeckOfCards = DeckOfCards()
objDeckOfCards.distributeCards()        
objDeckOfCards.printcards()     
        
        
        
        
        

