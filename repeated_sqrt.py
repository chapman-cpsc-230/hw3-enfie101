"""
File: repeated_sqrt.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code takes the squareroot of a number then squares it again.
"""

from math import sqrt

for n in range(1,60):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2

print '%d times sqrt and **2: %.16f' % (n, r)

#This code takes the squareroot of a natural number, then squares that result, and continues that process until it gets to the end of the range, whcih in this case is 60.
#When this process happens 59 times, the output is 1.0.  However, due to rounding errors, the output will not always be the most accurate should n be too big.
