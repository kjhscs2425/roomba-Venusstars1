# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(4)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius=5)

###
# Start your code here
import turtle
turtle.forward (40)
turtle.right(90)
turtle.forward (120)
turtle.left (90)
turtle.forward (40)
turtle.right (90)
turtle.forward (40)
turtle.left(90)
turtle.forward (240)

turtle.left (90)
turtle.forward (40)
turtle.right (90)
turtle.forward (40)
turtle.left(90)
turtle.forward (240)

turtle.left (90)
turtle.forward (40)
turtle.right (90)
turtle.forward (40)
turtle.left (90)
turtle.forward (240)

turtle.left (90)
turtle.forward (40)
turtle.right (90)
turtle.forward (40)

turtle.left (180)
turtle.forward (280)
for i in range (3):
    turtle.right (90)
    turtle.forward (40)
    turtle.right (90)
    turtle.forward (280)
    turtle.left (90)
    turtle.forward (40)
    turtle.left (90)
    turtle.forward (280)

turtle.left (180)
turtle.forward (120)
turtle.left (90)
turtle.forward (80)
turtle.left (180)
turtle.forward (200)
turtle.right(90)
turtle.forward (200)
turtle.left (180)
turtle.forward (200)
turtle.right (90)
turtle.forward (200)

   

 
 
# End your code here
###
 
window.exitonclick()