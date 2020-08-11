# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:28:13 2020

@author: Niraj Kumar
--String Replacement
Replacing Username with Name
"""

templateString = "Hello <<UserName>> How are you ? "
while(1):
    userName = input("Enter the UserName\n")
    if( len(userName) >= 3 ):
        break;
    else:
        print("The length of the name should be atleast 3")

newTemplateString = templateString.replace("<<UserName>>",userName)
print(newTemplateString)



