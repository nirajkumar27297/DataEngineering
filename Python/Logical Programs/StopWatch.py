# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:55:57 2020

@author: Niraj Kumar
Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks

"""

import time

start = input("Press any key to start ")
startTime = time.clock()
end = input("Press any key to stop ")
endTime = time.clock()
print("The elapsed time is ", round(endTime - startTime,2),"s")
