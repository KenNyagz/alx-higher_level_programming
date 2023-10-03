#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numbercp = -number
else:
    numbercp = number
 
modlo = numbercp % 10
print(f"Last digit of {number} is {modlo}", end = ' ')
if modlo == 0:
    print("and is 0")
elif modlo < 6 and modlo != 0:
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")
