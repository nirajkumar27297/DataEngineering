# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 23:10:35 2020

@author: Niraj Kumar
Create a JSON file having Inventory Details for Rice, Pulses and Wheats
with properties name, weight, price per kg
"""
import csv

class StockValueCalculation:
    def calculateTotalValue(self,filepath):
        try:
            with open(filepath,mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                lineCount = 0
                totalValue = 0
                for row in csv_reader:
                    if(lineCount == 0):
                        columns =','.join(row)
                        print("{},value".format(columns))
                    else:
                        stockValue = int(row['NumberofStocks']) * int(row['SharePrice'])
                        totalValue += stockValue
                        print("{},{},{},{}".format(row["ShareName"],row['NumberofStocks'],row['SharePrice'],stockValue))
                    lineCount += 1
                print("The total value of stock is",totalValue)
        except(IOError):
            print("Can't find the file specified")
            

stockObject = StockValueCalculation()
stockObject.calculateTotalValue("stocks.csv")

                    

    
