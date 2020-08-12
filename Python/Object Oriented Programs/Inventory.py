# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:35:39 2020

@author: Niraj Kumar
Create a JSON file having Inventory Details for Rice, Pulses and Wheats
with properties name, weight, price per kg.

"""
import json
import os
class Inventory:
    def __init__(self,name,weight,pricePerKg):
        self.name = name
        self.weight = weight
        self.priceperKg = pricePerKg
            
    def addDetails(self,inventory):
        try:
            if os.path.exists("inventory.json") == False:
                print("File Created")
                open("inventory.json", "w").close
            with open("inventory.json","r") as outputFile:
                sizeOfFile = os.stat("inventory.json").st_size
                if(sizeOfFile == 0):
                    data = {}
                else:
                    data = json.load(outputFile)
                dictionaryData ={}
                dictionaryData["name"] = self.name
                dictionaryData["weight"] = self.weight
                dictionaryData["pricePerKg"] = self.priceperKg
                if inventory not in data:
                    data[inventory] = []
                    data[inventory].append(dictionaryData)
                else:
                    temp = data[inventory]
                    temp.append(dictionaryData)
            
            with open('inventory.json', 'w') as f: 
                json.dump(data,f,indent = 4)
                print(data[inventory])
                
        except(IOError):
            print("File can't be found")
                

class Cereals(Inventory):
    def __init__(self,inventory,name,weight,pricePerKg):
        super().__init__(name,weight,pricePerKg)
        self.inventory = inventory


while(1):
    ch = input("1.Enter details for Rice\n2.Enter details for Wheat\n3.Enter details for Pulses\nElse to exit")
    name,weight,pricePerKg = [x for x in input("Enter the name,weight,PricePerKg").split()]
    if(ch == '1'):
        rice = Cereals("Rice",name,weight,pricePerKg)
        rice.addDetails("Rice")
    elif(ch == '2'):
        wheat = Cereals("Wheat",name,weight,pricePerKg)
        wheat.addDetails("Wheat")
    elif(ch == '3'):
        pulse = Cereals("Pulse",name,weight,pricePerKg)
        pulse.addDetails("Pulse")
    ch = input("Do you wanr to enter more details if yes press y")
    if(ch.lower() != 'y'):
        break
        
    
    
