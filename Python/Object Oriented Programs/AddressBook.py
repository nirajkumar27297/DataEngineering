# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:30:10 2020

@author: Niraj Kumar

"""

class Address:
    
    def __init__(self,blockNo,city,state,pinCode):
        self.__blockNo = blockNo
        self.__city = city
        self.__state = state
        self.__pinCode = pinCode
    
    def getCity(self):
        return self.__city
    
    def getblockNo(self):
        return self.__blockNo
    
    def getState(self):
        return self.__state
    
    def getPinCode(self):
        return self.__pinCode
    
    def setCity(self,city):
        self.__city = city
    
    def setBlockNo(self,blockNo):
        self.__blockNo = blockNo
    
    def setState(self,state):
        self.__state = city
    
    def setPinCode(self,pinCode):
        self.__pinCode = pinCode
    

class Person:
    def __init__(self,firstName,lastName,phoneNo,blockNo,city,state,pinCode):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phoneNo = phoneNo
        self.__Address = Address(blockNo,city,state,pinCode)

        
    def getPhoneNo(self):
        return self.__phoneNo
    #overwrite tostring
    def __str__(self):
        output = "Name: " +self.__firstName + " " + self.__lastName + "\nPhoneNo: " + self.__phoneNo + "\nAddress: " + self.__Address.getblockNo()+","+\
        self.__Address.getCity()+","+self.__Address.getState()+","+self.__Address.getPinCode()
        return output
    
    
    
    def setPhoneNo(self,phoneNo):
        self.__phoneNo = phoneNo
    
    def getFirstName(self):
        return self.__firstName
    
    def getlastName(self):
        return self.__lastName
    
    def getAddress(self):
        return self.__Address
    
    
    

class AddressBook:
    
    def __init__(self):
        self.listPeople = []
        
        
    def addAddressData(self,firstName,LastName,phoneNo,blockNo,city,state,pinCode):
        person = Person(firstName,LastName,phoneNo,blockNo,city,state,pinCode)
        self.listPeople.append(person)
    
    def searchPerson(self,phoneNo):
        for person in self.listPeople:
            if(person.getPhoneNo() == phoneNo):
                print(person)
                return
        print("Person Not Found")
        
    def editAddressData(self,columnField,columnFieldValue,phoneNo):
        for person in self.listPeople:
            if(person.getPhoneNo() == phoneNo):                
                if(columnField == '1'):
                    person.setPhoneNo(columnFieldValue)
                
                elif(columnField == '3'):
                    person.getAddress().setCity(columnFieldValue)
                
                elif(columnField == '4'):
                    person.getAddress().setState(columnFieldValue)
                
                elif(columnField == '2'):
                    person.getAddress().setBlockNo(columnFieldValue)
                
                elif(columnField == '5'):
                    person.getAddress().setPinCode(columnFieldValue)
                else:
                    print("Invalid column field")
                    return
                print("Column ",columnField,"updated sucessfully")
                return
        print("Person Not Found")
        
    
    def sortPersonlist(self):
        sortedPersonList =sorted(self.listPeople, key = lambda i: (i.getFirstName() ,i.getlastName() , i.getAddress() ))
        for person in sortedPersonList:
            print(person)
            print("----------------------------")
        
        
        
addressBook = AddressBook()
while(1):
    print("1.Enter data to Addressbook\n2.Search data in AddressBook by PhoneNumber\n3.Update data in book\n4.Print Address book\nElse to exit")
    ch = input()
    if(ch == '1'):
        while(1):
            firstName,lastName = [x for x in input("Enter the name of the person ").split()]
            phoneNo = input("Enter the phone number of the person ")
            blockNo,city,state,pinCode = [x for x in input("Enter the address separated by commas ").split(",")]
            addressBook.addAddressData(firstName.capitalize(),lastName.capitalize(),phoneNo,blockNo,city,state,pinCode)
            customerChoice = input("Do you want to enter more person if yes press y/Y ")
            if(customerChoice.upper() != 'Y'):
                break
            
    elif(ch == '2'):
        while(1):
            phoneNo = input("Enter the phone number of the person ")
            addressBook.searchPerson(phoneNo)
            customerChoice = input("Do you want to search for more person if yes press y/Y ")
            if(customerChoice.upper() != 'Y'):
                break
    elif(ch == '3'):
         while(1):
            phoneNo = input("Enter the phone number of the person ")
            columnField = input("1.Phone Number\n2.Block Number\n3.City\n4.State\n5.PinCode\n")
            columnFieldValue = input("Enter the column value ")
            addressBook.editAddressData(columnField,columnFieldValue,phoneNo)
            customerChoice = input("Do you want to update fields for more person if yes press y/Y ")
            if(customerChoice.upper() != 'Y'):
                break
    elif(ch == '4'):
        addressBook.sortPersonlist()
        
    else:
        print("Invalid Choice")
        break;
    
       
        
    