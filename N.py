import turtle
import time

def drawnN():
    n=turtle.Turtle()
    n.penup()
    n.goto(-30,50) #centering in the screen
    n.pendown()
    n.pensize(5)
    n.pencolor("black")
    n.right(90)
    n.forward(150)
    n.goto(-30,50)
    n.right(-35)
    n.forward(180)
    n.right(215)
    n.forward(150)

    time.sleep(3)
drawnN()
