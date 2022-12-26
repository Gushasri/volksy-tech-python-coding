#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
m = n % 10
if (m > 5):
    print("FLast digit of {} is".format(n),m,"and is greater than 5")
elif(m == 0):
    print("First 3 letters {} is".format(n),m,"and is 0")
else:
    print("First 3 letters {} is".format(n),m,"and is less than 6 and not 0")


