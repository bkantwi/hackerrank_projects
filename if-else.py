#!/bin/python3

# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird
# Input Format
#
# A single line containing a positive integer, .
#
# Constraints
# 1 <= n <= 100

import math
import os
import random
import re
import sys

# n = random.randint(1, 100)
#
# print(n)
#
# odd = (n % 2) == 1
# even = (n % 2) == 0
#
# if (n % 2) == 1:
#     print("Weird")
#
# elif ((2 <= n <= 5) & even):
#     print("Not Weird")
#
# elif ((6 <= n <= 20) & even):
#     print("Weird")
#
# elif ((n > 20) & even):
#     print("Not Weird")


# OR


if __name__ == '__main__':
    n = int(input().strip())

num =n%2

if num!=0:
    print("Weird")
elif num ==0 and n in range(2,6):
    print("Not Weird")
elif num == 0 and n in range(6,21):
    print("Weird")
elif num==0 and n >= 20:
    print("Not Weird")
