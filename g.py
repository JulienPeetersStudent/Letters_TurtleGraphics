import turtle
def G(): 
    t=turtle.Turtle()
    t.speed(100)
    t.penup()
    t.goto(-50,50) #centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("green")
    t.circle(75,-190,100)
    t.penup()
    t.goto(-50,50)
    #t.


G()
turtle.done()