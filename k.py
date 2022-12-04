import turtle

scrn = turtle.Screen()
pen = turtle.Turtle()
pen.pencolor('blue')
pen.pensize(3)
pen.penup()
pen.backward(50)
pen.pendown()

pen.left(90)
pen.forward(120)
pen.backward(80)
pen.right(40)
pen.forward(100)
pen.backward(75)
pen.right(100)
pen.forward(80)

turtle.exitonclick()
