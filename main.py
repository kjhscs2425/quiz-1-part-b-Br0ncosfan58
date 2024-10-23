import turtle
from turtle import *

# YOUR CODE HERE
def draw_square():
    for i in range (4):
        forward(100)
        right(90)

draw_square()
penup()
forward(100)
right(90)
forward(100)
right(90)
forward(50)
pendown()

right(45)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)

penup()
right(135)
forward(100)
right(125)

turtle.exitonclick()