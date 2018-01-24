# -----------------------------------------+
# Joel Lechman, Tanner Seramur             |
# CSCI 107, Assignment 6                   |
# Last Updated: 10, 16, 2015               |
# -----------------------------------------|
# Use functions, user input, and random    |
# and turtle modules to create             |
# art similar to Piet Mondrain's work.     |
# -----------------------------------------+


# Do we need to account for black rectangles?

import turtle
import random

number_of_rectangles = int(input("How many rectangles should be drawn? "))
max_width_float = float(input("What should the maximum WIDTH of the rectangles be? (in pixels) "))
max_height_float = float(input("What should the maximum HEIGHT of the rectangles be? (in pixels) "))

max_width = int(max_width_float)
max_height = int(max_height_float)
# The if/than statements make any user input for max_height/max_width that is < 10, equal to ten (so all of the rectangles are visable on the screen)
if max_width < 10:
    max_width = 10
if max_height < 10:
    max_height = 10


# Created a function to draw one rectangle of a specific size at a specfiic spot of a specific color
def draw_rectangle(some_turtle, width, height, top_left_x, top_left_y, color):
    some_turtle.penup()
    some_turtle.goto(top_left_x, top_left_y)
    some_turtle.pendown()
    some_turtle.color(color)
    some_turtle.begin_fill()
    for i in range(2):
        some_turtle.forward(width)
        some_turtle.right(90)
        some_turtle.forward(height)
        some_turtle.right(90)
    some_turtle.end_fill()
    some_turtle.hideturtle()

# Setting up the window and turtle 
window = turtle.Screen()
window.bgcolor("black")
turtle = turtle.Turtle()
turtle.speed(0)


# Generating random rectangle width and height with functions
def random_width():
    random_width = random.randint(10,max_width)
    return(random_width)

def random_height():
    random_height = random.randint(10,max_height)
    return(random_height)

# Generating random x,y positions with functions
def random_x_pos():
    random_x_pos = random.randint(int(-1*window.window_width()/2),(int(window.window_width()/2))-10) #the minus ten value is so that the x pos cant be set to have the rectangle off the screen (ex. if x is set for the far right border)
    return(random_x_pos)

def random_y_pos():
    random_y_pos = random.randint((int(-1*window.window_height()/2)+10),int(window.window_height()/2)) # the plus ten value is so that the y pos cant be set to have the rectangle off the screen (ex. if y is set for the bottom border)
    return(random_y_pos)
   
# Generating random colors using a function and random float numbers
def random_color():
    red = random.random()
    green = random.random()
    blue = random.random()
    random_color = (red,green,blue)
    return(random_color)

# A function so that we only have to call one thing to run the program.
def random_rectangles():
    for i in range(number_of_rectangles):
        draw_rectangle(turtle, random_width(), random_height(), random_x_pos(), random_y_pos(), random_color())



random_rectangles()

window.exitonclick()




