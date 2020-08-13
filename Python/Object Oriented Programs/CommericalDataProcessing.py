# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 01:13:07 2020

@author: hp
"""
import csv
import os
import json
class CustomerInformation:
    def __init__(self,filepath = "customer.csv"):
        self.filepath = filepath
        if os.path.exists("customer.csv") == False:
                print("File Created")
                file = open("customer.csv", "w")
                writer = csv.writer(file)
                writer.writerow(["name","phoneNo","stockAccountNumber"])
                file.close()
        
    
    def searchCustomer(self,name,phoneNo):
        with open(self.filepath,mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            lineCount = 0
            for row in csv_reader:
                if(lineCount != 0 ):
                    if(name == row['Name'] and phoneNo == row['phoneNo']):
                        stockAccountNumber = row["stockAccountNumber"]
                        return stockAccountNumber
                        csv_file.close()
        while(1):
            ch = input("1.Buy a stock")
            if(ch == 1):
                stockAccount = StockAccount()
                stockAccount.buy(stockAccountNumber,"TATA",300)
            choice = input("Do you want to enter more data")
            if(choice != 'y'):
                return
    
    def addCustomer(self,name,phoneNo):
        file = open(self.filepath)
        reader = csv.reader(file)
        lines = len(list(reader))
        file.close()
        stockAccountNumber = lines+1
        with open(self.filepath,'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows([name,phoneNo,stockAccountNumber])
        return stockAccountNumber
        
        
       
class StockAccount:
    def __init__(self,filepath = "StockAccount.json"):
        self.filepath = filepath
        
        if os.path.exists("StockAccount.json") == False:
                print("File Created")
                open("StockAccount.json", "w").close
    
    def buy(self,stockAccountNumber,stockSymbol,amount):
        try:
            stock = StockValueCalculation()
            numberOfShares = stock.shareDetails(stockSymbol,amount)
            print(numberOfShares)
            if(numberOfShares == -1):
                print(2)
                return
            with open("StockAccount.json","r") as outputFile:
                sizeOfFile = os.stat("StockAccount.json").st_size
                if(sizeOfFile == 0):
                    data = {}
                else:
                    data = json.load(outputFile)
                
                dictionaryData ={}
                dictionaryData["stockSymbol"] = stockSymbol
                dictionaryData["NumberOfShares"] = numberOfShares
                dictionaryData["transactionDate"] = 0
                if stockAccountNumber not in data:
                    data[stockAccountNumber] = []
                    data[stockAccountNumber].append(dictionaryData)
                else:
                    temp = data[stockAccountNumber]
                    temp.append(dictionaryData)
            
            with open('StockAccount.json', 'w') as f: 
                json.dump(data,f,indent = 4)
                print(data[stockAccountNumber])
                
        except(IOError):                                                                                                                                                                
            print("File can't be found")
    def sell(self,stockAccountNumber,stockSymbol,amount):
        try:
            with open("StockAccount.json","r") as outputFile:
                sizeOfFile = os.stat("StockAccount.json").st_size
                if(sizeOfFile == 0):
                    data = {}
                else:
                    data = json.load(outputFile)
                
                print(data[stockAccountNumber])
                stock = StockValueCalculation()
                numberOfShares = stock.shareDetails(stockSymbol,amount,2)
                for i in data[stockAccountNumber]:
                    if( i['stockSymbol'] == stockSymbol and i['NumberOfShares'] != 0):
                        priornumberOfShares = i['NumberOfShares'] 
                        break
                        
                if(numberOfShares > priornumberOfShares):
                    print("You don't have enough shares to sell")
                    return
                dictionaryData = {}
                numberOfShares = stock.shareDetails(stockSymbol,amount,1)
                dictionaryData["stockSymbol"] = stockSymbol
                dictionaryData["NumberOfShares"] = priornumberOfShares- numberOfShares
                dictionaryData["transactionDate"] = 0
                temp = data[stockAccountNumber]
                temp.append(dictionaryData)
            
            with open('StockAccount.json', 'w') as f: 
                json.dump(data,f,indent = 4)
                print(data[stockAccountNumber])
                
        except(IOError):                                                                                                                                                                
            print("File can't be found")
    
    def printReport():
        try:
            with open("StockAccount.json","r") as outputFile:
                sizeOfFile = os.stat("StockAccount.json").st_size
                if(sizeOfFile == 0):
                    data = {}
                else:
                    data = json.load(outputFile)
                print(data)
        except(IOError):                                                                                                                                                                
            print("File can't be found") 

class StockValueCalculation:
    def __init__(self,filepath = "CompanyShares.csv"):
        self.filepath = filepath
    def shareDetails(self,stockSymbol,amount,flag = 0):
        try:
            r = csv.reader(open(self.filepath)) # Here your csv file
            lines = list(r)
            nrows = len(lines)
            
            shareAllocated = -1
            for i in range(nrows):
                if(i != 0):
                    if(len(lines[i]) != 0 and lines[i][0].upper() == stockSymbol and lines[i][1] != '0'):
                        shareAllocated = int(amount) / int(lines[i][2])
                        if(flag == 0):
                            lines[i][1] = float(lines[i][1]) - shareAllocated
                        elif(flag == 1):
                            lines[i][1] = float(lines[i][1]) + shareAllocated
                            
                        break
                    
          
            with open(self.filepath,'w', newline='') as csvfile:
                #creating  a csv writer object
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(lines)
            return shareAllocated
        except(IOError):
            print("Can't find the file specified")
    
    
                        
   
#main function
customer = CustomerInformation()   
name,phoneNo = [x for x in input("Enter you name and phonenumber").split()]     
ch = input("Are you a new customer")
if(ch.lower() == 'y'):
    
    stockAccountNumber = customer.addCustomer(name,phoneNo)
else:
    stockAccountNumber = customer.searchCustomer(name,phoneNo)
    
while(1):
        ch = input("1.Buy a stock\n2.Sell a stock\n3.Print the report")
        stockAccount = StockAccount()
        if(ch == '1'):
            [stockSymbol,amount] = [x for x in input("Enter the Stock Symbol and amount").split()]
            stockAccount.buy(stockAccountNumber,stockSymbol,amount)
        elif(ch == '2'):
            [stockSymbol,amount] = [x for x in input("Enter the Stock Symbol and amount").split()]
            stockAccount.buy(stockAccountNumber,stockSymbol,amount)
        elif(ch == '3'):
            stockAccount.printReport()
        choice = input("Do you want to enter more data")
        if(choice != 'y'):
            break   
        
    
    