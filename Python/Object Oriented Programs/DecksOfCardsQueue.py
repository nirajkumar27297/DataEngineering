
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
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.count = 0
class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__count = 0
    def enqueue(self,data):
        newNode = Node(data)
        if(self.__front == None and self.__rear==None):
            self.__front = newNode
            
        else:
            self.__rear.next = newNode
        self.__rear = newNode
        self.__count += 1
    
    def isEmpty(self):
        return self.__count == 0
    
    def dequeue(self):
        if(self.isEmpty()):
            print("Underflow.....Queue is Empty")
            return -1
        data = self.__front.data
        self.__front = self.__front.next
        self.__count -= 1
        return data
    
    def display(self):
        temp = self.__front
        if(self.isEmpty()):
            print("Underflow.....Queue is Empty")
            return
        temp = self.__front
        while(temp is not None):
            print(temp.data)
            temp = temp.next
        return
    
    def getfront(self):
        return self.__front
            
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
            #To make Ace most superior
            if(cardNumber == 1):
                cardNumber = 14
                                                                                                                                                                                                                                                 
            return cardType,cardNumber
    
    def distributeCards(self):
        q = Queue()
        playerCards ={}
        for i in range(13):
            cardType,cardNumber = self.generateCard()
            if cardType not in playerCards:
                playerCards[cardType] = [cardNumber]
            else:
                playerCards[cardType].append(cardNumber)
        #Sorting while distributing cards only        
        for cardType in playerCards:
            playerCards[cardType].sort()
            for cardNumber in playerCards[cardType]:
                if(cardNumber == 14):
                    cardNumber = "ACE"
                elif(cardNumber == 11):
                    cardNumber = "King"
                elif(cardNumber == 12):
                    cardNumber = "Queen"
                elif(cardNumber == 13):
                    cardNumber = "Jack"
                else:
                    cardNumber = str(cardNumber)
                q.enqueue(cardType+" "+cardNumber)
        
        return q
 
    def printcards(self,q):
        q.display()
    
    def gameplay(self):
        q = Queue()
        for i in range(4):
            print("For the Player {}".format(i+1))
            q.enqueue("Player"+str(i+1))
            q = self.distributeCards()
            self.printcards(q)
            print("***********************************************")


objDeckOfCards = DeckOfCards()
objDeckOfCards.gameplay()
        
    
    
        
        
        
        
        

