import turtle
def G(): 
    t=turtle.Turtle()
    t.speed(100)
    t.penup()
    t.goto(-50,50) #centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("green")
    t.circle(75,-180,100)
    t.penup()
    t.goto(-50,50)
    t.pendown()
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(30)


G()
turtle.done()