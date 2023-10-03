#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    numbercp = -number
else:
    numbercp = number
 
modlo = numbercp % 10

if modlo is 0:
     print("Last digit of {number} is {modlo} and is 0")
elif modlo < 6 and not 0:
     print("Last digit of {number} is {modlo} and is less than 6 and not 0"
else:
     print("Last digit of {number} is {modlo} and is greater than 5"
