#!/bin/python3

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
