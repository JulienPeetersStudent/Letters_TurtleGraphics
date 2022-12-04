import turtle as T;

def J():
   window = T.Screen()
   obj = T.Turtle()

   obj.forward(50)
   obj.left(90)
   obj.forward(70)
   obj.penup()
   obj.setpos(obj.pos()[1] + 20, 0)
   obj.setheading(0)
   obj.pendown()
   obj.right(90)
   obj.forward(100)
   T.done()

J()