import turtle
rocket=turtle.Turtle()
space=turtle.Screen()
space.bgpic("bg.gif")

sman=turtle.Turtle()
space.addshape("man.gif")
sman.shape("man.gif")
sman.penup()
sman.goto(-103,255)

space.addshape("roc.gif")
rocket.shape("roc.gif")
rocket.penup()
rocket.goto(180,-250)
rocket.speed(1000)

def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)
def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)
def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)
def right():
    rocket.forward(10)
turtle.listen()                
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
while True:
  space.update()
  if rocket.distance(sman)<10:
    space.bgpic("thanku.gif")
turtle.done()
