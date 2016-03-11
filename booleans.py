
"""
File: booleans.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code was used to simply gain a better understanding of what different boolean expressions will do.
"""

C = 41 #There will be no output. This expression is setting the variable 'C' equal to 41.
C == 40 #The output will be 'False'. 40 is being compared to 0.
C != 40 and C < 41 #The output will be 'False',since both conditions are not true.
C != 40 or C < 41 #The output will be 'True', since the first condition is true, despite the second condition being false.
not C == 40 #The output will be 'True'. Because of the 'not' at the beginning, the output is reversed. The condition is False, but because of the 'not' the output will be 'True'.
not C > 40 #The output will be 'False'.  The condition is true, but because of the 'not' at the beginning of the expression, the output will be reversed.
C <= 41 #The output will be  'True'.
not False #The output will be 'True'.
True and False #The output will be 'False'.
False or True #The output will be 'True'.
False or False or False #The output will be 'False'.
True and True and False #The output will be 'False'.
False == 0 #The output will be 'True'.
True == 0 #The output will be 'False'.
True == 1 #The output will be 'True'.
