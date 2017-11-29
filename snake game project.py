import random
import turtle
wn=turtle.Screen()
snake=turtle.Turtle()

def makefood():
    tfood=[random.randint(1,40),random.randint(1,40)]
    return tfood
def goforward():
    snake.forward(100)
    
        
        
    
snakesize=1
snakelocation=[15,20]
snakerotation=0
bricks=[[0,0],[30,40]]
food=makefood()

wn.onkey(goforward,"Up")
wn.listen()
wn.mainloop
