#Tanner Seramur6

# The width of each branch varies based on the order of the tree (see within draw_branch)


import turtle

def draw_branch(branch_length, turtle, order):
    if order >=1:
        #setting up the width of each branch to decrease with each order (to make it more realistic)
        width= order*2-1
        turtle.pensize(width)
        #drawing the tree of order 1       
        turtle.forward(branch_length)
        turtle.right(20)
        #Recursively calling Draw_branch 2 times for a branching factor of 2
        draw_branch(branch_length-5,turtle,order-1)
        turtle.left(40)
        draw_branch(branch_length-5,turtle,order-1)
        turtle.right(20)
        turtle.backward(branch_length)

def tree():
    order = int(input("Please choose an order of tree to print. (Select an integer between 1 and 6): "))
    #Getting the drawing turtle to the starting point so that the full tree fits on the screen
    drawing_turtle = turtle.Turtle()
    drawing_turtle.speed(0)
    drawing_turtle.hideturtle()
    window = turtle.Screen()
    drawing_turtle.right(90)
    drawing_turtle.up()
    drawing_turtle.forward(200)
    drawing_turtle.right(180)
    drawing_turtle.down()
    #Pen color of brown to make it look like an actual tree instead of a burnt one
    drawing_turtle.color("#996633")
    #Increasing/decresing the first number in draw_branch below will change the size of the tree (the length of the branches)
    draw_branch(100,drawing_turtle,order)
    window.exitonclick()

tree()
