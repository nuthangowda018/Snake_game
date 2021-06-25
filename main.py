from turtle import Turtle,Screen
from snake import Snake
from food import  Food
from scoreboard import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)


is_mov =True
while is_mov:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.timlist[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.timlist[0].xcor()>280 or snake.timlist[0].xcor()<-280 or snake.timlist[0].ycor()>280 or snake.timlist[0].ycor()<-280 :
        is_mov=False
        score.game_over()

    for tim in snake.timlist[1:]:
        if snake.timlist[0].distance(tim)<10:
            is_mov=False
            score.game_over()









screen.exitonclick()