import turtle

scrn = turtle.Screen()
pen = turtle.Turtle()
pen.pencolor('green')
pen.pensize(3)
pen.penup()
pen.backward(50)
pen.pendown()

pen.left(90)
pen.forward(120)
pen.right(135)
pen.forward(70)
pen.left(90)
pen.forward(70)
pen.right(135)
pen.forward(120)

turtle.exitonclick()