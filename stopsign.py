
import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)


# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = 50

# Initialize the turtle.

    
# Move the turtle to the starting point.
turtle.penup()
turtle.setpos(-50,120)



# Draw the octagon.
turtle.pendown()
for x in range(0,9):
    turtle.forward(100)
    turtle.right(45)
turtle.penup()
turtle.setpos(-30,-15)
turtle.pendown()


# Display 'STOP'

turtle.write('STOP',font=('Arial',18,'normal'))

