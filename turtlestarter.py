import turtle

def draw_reg_polygon(t,num_sides,side_len):
    for i in range(num_sides):
        t.forward(side_len)
        t.right(360.0/num_sides)

# Ask user for input here.

# Now create a graphics window.
bob = turtle.Pen()

# Put the rest of your code can go here

# side = 10
for j in range(20):
    draw_reg_polygon(bob,6,10 + 5*j)
    bob.left(18)
    # draw_square(bob,side)
    # side += 5

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
