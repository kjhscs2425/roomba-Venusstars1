# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
import turtle
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
#Start your code here
turtle.speed (7)
turtle.forward (560)
#for i in range(19):
    # turtle.left (90)
    # turtle.forward (40)
    # turtle.left (90)
    # turtle.forward (560)
    # turtle.right(90)
    # turtle.forward (40)
    # turtle.right(90)
    # turtle.forward (560)

height=15
width = 20
square = 40

forward ((height-1)*square)
for i in range (1, min(height, width) +1):
    vertical_arm_length = (height-i) * square
    horizontal_arm_length = (height-i) * square
    left (90)
    forward(horizontal_arm_length)
    left (90)
    forward(vertical_arm_length)


 
# End your code here
###
 
window.exitonclick()