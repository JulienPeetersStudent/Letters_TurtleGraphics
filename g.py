'''
Copy this template for each letter. Then change the functions.
The placeholders in this file just draw rectangles. You should remove these
commands and replace them with your own.
Make sure that you use relative sizes, i.e. based on the parameter size.
'''


def draw(turtle, size=400):
    '''
    Draw lowercase letter.
    The parameter ``turtle'' is a Turtle object.
    The parameter size is the maximum height of the letter. All turtle
    movements should be relative to the size.
    '''
    turtle.pensize(1)
    turtle.setheading(0)
    turtle.pencolor('grey')
    turtle.pendown()
    for s in (1, 2): # Do the following twice for loop twice.
        for side in (size / 2, size):
            turtle.forward(side)
            turtle.left(90)
    turtle.penup()
    turtle.setx(turtle.pos()[0] + size / 2 + size / 40)


def draw_capital(turtle, size=400):
    '''Draw uppercase letter'''
    draw(turtle, size)  # change this
