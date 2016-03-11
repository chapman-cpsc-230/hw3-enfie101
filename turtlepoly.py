"""
File: turtlepoly.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code should produce a 'n' sided polygon with each side of length 'side_len' based on the user's input.
"""

import turtle

def draw_reg_polygon(t,num_sides,side_len):
    for i in range(num_sides):
        t.forward(side_len)
        t.right(360.0/num_sides)

# Ask user for input here.
n_str = raw_input("Enter the number of sides (must be odd):")
n = int(n_str)

l_str = raw_input("Enter the length of the sides:")
l = int(l_str)

# Now create a graphics window.
bob = turtle.Pen()

# The rest of your code can go here

# side = 10
for j in range(1):
    draw_reg_polygon(bob,n,l)
    bob.left(18)
    # draw_square(bob,side)
    # side += 5

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
