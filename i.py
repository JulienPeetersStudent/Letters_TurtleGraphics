def draw(turtle, size=400):
    '''
    Draw lowercase letter.
    The parameter ``turtle'' is a Turtle object.
    The parameter size is the maximum height of the letter. All turtle
    movements should be relative to the size.
    '''
    origpos = turtle.position()
    turtle.pensize(1)
    turtle.setheading(0)
    turtle.pencolor('grey')
    turtle.forward(size / 3)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(size * 4 / 5)
    turtle.penup()
    turtle.forward(size * 1/8)
    turtle.pendown()
    turtle.circle(size / 40)
    turtle.penup()
    turtle.goto(origpos[0] + size / 2, origpos[1])


def draw_capital(turtle, size=400):
    '''Draw uppercase letter'''
    draw(turtle, size)  # change this

if __name__ == '__main__':
    import turtle
    t = turtle.Turtle()
    t.penup()
    draw(t)