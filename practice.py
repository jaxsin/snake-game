import turtle

wn=turtle.Screen()
snake=turtle.Turtle()

def gof():
    snake.forward(30)
wn.onkey(gof,"Up")
wn.listen()
wn.mainloop()