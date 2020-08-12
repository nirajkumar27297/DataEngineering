# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:12:46 2020

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:35:39 2020

@author: Niraj Kumar
Create a JSON file having Inventory Details for Rice, Pulses and Wheats
with properties name, weight, price per kg.
he Inventory Manager will use InventoryFactory to create Inventory
Object from JSON. The InventoryManager will call each Inventory Object in its list
to calculate the Inventory Price and then call the Inventory Object to return the
JSON String. The main program will be with InventoryManager

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
            if os.path.exists("inventoryManager.json") == False:
                print("File Created")
                open("inventoryManager.json", "w").close
            with open("inventoryManager.json","r") as outputFile:
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
            
            with open('inventoryManager.json', 'w') as f: 
                json.dump(data,f,indent = 4)
                print(data[inventory])
                
        except(IOError):
            print("File can't be found")
                

class Cereals(Inventory):
    def __init__(self,inventory,name,weight,pricePerKg):
        super().__init__(name,weight,pricePerKg)
        self.inventory = inventory


while(1):
    invenotryName,name,weight,pricePerKg = [x for x in input("Enter the Inventory Name,Goods name,weight,PricePerKg separated by comma").split(",")]
    cereals = Cereals(invenotryName,name,weight,pricePerKg)
    ch = input("Do you want to enter more details if yes Press y/Y else n")
    if(ch.lower() != 'y'):
        break
        
    
    
