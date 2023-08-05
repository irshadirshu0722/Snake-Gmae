from turtle import Turtle,Screen
import time
from scoreboard import scoreboard
import random
from snake import SnakeGame
from food import food
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = SnakeGame()
food  = food()
Scoreboard = scoreboard()

screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Right,"Right")
screen.onkey(snake.Left,"Left")

egg_init_position = [(100,100)]

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect the collision with food
    if snake.segments[0].distance(food)<15:
        Scoreboard.score_update()
        snake.Add_segment()
        food.refresh()
    # detect collison with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280  or snake.head.ycor() >280 or snake.head.ycor() <-280 :
        game_is_on = False
    # detect collsion with tail

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) <10:
           game_is_on = False

Scoreboard.game_over()
    #result = snake.move()
    # segment_position = snake.get_position()

    # if snake.segments[0].pos() in segment_position:
    #
    #     screen.clear()
    #     break


    # if result== True:
    #     snake.change_egg()
    #     snake.increse_segment()
    #     snake.scoreupdate()







screen.exitonclick()


