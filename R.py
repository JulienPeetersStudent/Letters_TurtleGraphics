import turtle
import time

def drawnR():
    t=turtle.Turtle()
    t.penup()
    t.goto(-30,50) #centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("red")
    t.right(90)
    t.forward(150)
    t.goto(-30,50)
    t.right(-90)
    t.circle(-50,180,100)
    t.penup()
    t.goto(0,-40)
    t.left(135)
    t.pendown()
    t.forward(70)

    time.sleep(3)
drawnR()