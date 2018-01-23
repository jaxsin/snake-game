import random
import turtle
wn=turtle.Screen()
snake=turtle.Turtle()
myturt=turtle.Turtle()




myturt.shape("square")
myturt.penup()
tfood_id = []
tfood_coord=[]

for i in range(random.randint(11,12)):
    food = (random.randint(-300,200),random.randint(-300,300))
    myturt.setpos(food[0],food[1])
    this_stamp = myturt.stamp()
    tfood_coord.append((food[0],food[1]))
    tfood_id.append(this_stamp)

"""
count = 0               
for i in tfood_id:
    print(tfood_coord[count])
    myturt.clearstamp(tfood_id[count])
    count += 1


"""
def goforward():
    snake.forward(10)
    print(snake.pos())
    count=0
    for i in tfood_coord:
        if snake.pos() == i:
            snake.clearstamp(tfood_id[count])
            tfood_id.pop(count)
        count+=1
                         
def goleft():
    snake.left(90)
def goright():
    snake.right(90)
def gobackward():
    snake.backward(10)
        
    
snakesize=1
snakelocation=[15,20]
snakerotation=0
bricks=[[0,0],[30,40]]
#food=makefood()

myturt.setpos(0,0)
myturt.pendown()
myturt.shape("arrow")
wn.onkey(goforward,"Up")
wn.onkey(goleft,"Left")
wn.onkey(goright,"Right")
wn.onkey(gobackward,"Down")
wn.listen()
wn.mainloop



