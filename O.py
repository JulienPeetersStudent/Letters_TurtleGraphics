import turtle # load the turtle module
def drawnO():
    t=turtle.Turtle()
    t.penup()
    t.setpos(10,50)
    t.pendown()
    t.pensize(10)
    t.color("black")
    t.circle(100)
    t.exitonclick()
drawnO()