# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:03:30 2020

@author: Niraj Kumar
Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be:
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v^0.16
"""
try:
    temperature,velocity = [int(x) for x in input("Enter temperature and velocity").split()]
    if( (temperature > 50) or ( velocity > 120 or velocity < 3)):
        raise Exception
    
    windChill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * velocity ** 0.16
    print("The value of Wind Chill is ",round(windChill,2))

except(Exception):
    print("Temperature should be less than 50 and Velocity should between 3 and 50")


