#!/bin/python3

# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
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

n = random.randint(1, 100)

mod = n % 2

if mod > 0:
    print("Weird")

if (mod == 0 & n >=2 & n <5):
    print("Not Weird")

if (mod == 0 & n >=6 & n <20):
    print("Weird")

if (mod == 0 & n >20):
    print("Not Weird")
