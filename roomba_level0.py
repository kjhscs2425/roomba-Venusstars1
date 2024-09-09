# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
import turtle 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
 
 
 
# End your code here
###
for i in range(3):
    turtle.forward (160)
    turtle.left (90)
for i in range (2):
    turtle.forward (120)
    turtle.left(90)
for i in range (2):
    turtle.forward (80)
    turtle.left(90)
for i in range (2):
    turtle.forward(40)
    turtle.left(90)

window.exitonclick()