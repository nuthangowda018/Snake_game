from turtle import Turtle, Screen
POSITION=[(0,0),(-20,0),(-40,0)]
FORWARD_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180


class Snake:

   def __init__(self):
       self.timlist=[]
       self.create_tim()

   def create_tim(self):
       for position in POSITION:
           self.add(position)

   def add(self,position):
       tim = Turtle(shape="square")
       tim.penup()
       tim.color("white")
       tim.goto(position)
       self.timlist.append(tim)


   def extend(self):
       self.add(self.timlist[-1].position())


   def move(self):
       for t in range(len(self.timlist) - 1, 0, -1):
           x = self.timlist[t - 1].xcor()
           y = self.timlist[t - 1].ycor()
           self.timlist[t].goto(x, y)
       self.timlist[0].forward(FORWARD_DISTANCE)

   def up(self):
       if self.timlist[0].heading()!=DOWN:
            self.timlist[0].setheading(UP)

   def left(self):
       if self.timlist[0].heading() != RIGHT:
            self.timlist[0].setheading(LEFT)

   def right(self):
       if self.timlist[0].heading() != LEFT:
            self.timlist[0].setheading(RIGHT)

   def down(self):
       if self.timlist[0].heading() != UP:
            self.timlist[0].setheading(DOWN)