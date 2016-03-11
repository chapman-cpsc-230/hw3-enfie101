"""
File: turtlestar.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code will produce an 'n' pointed star. The user will input the number of points on the star as well as the size of each of the sides.
"""

import turtle

# Ask user for input here.
n_str = raw_input("Enter the number of points on the star (must be an odd number greater than 5):")
n = int(n_str)

l_str = raw_input("Enter the length:")
l = int(l_str)

# Now create a graphics window.
bob = turtle.Pen()

# Put the rest of your code can go here
bob.up()
bob.left(l/2.0)
bob.down()

# side = 10
for j in range(n):
    bob.forward(l)
    bob.left(180.0-(180.0/n))

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
