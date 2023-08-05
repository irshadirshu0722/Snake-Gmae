import random
from turtle import Turtle,Screen
import time

class SnakeGame:
    def __init__(self):
        self.segment_init_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]
        self.egg_position=[100,100]
        self.egg = Turtle("square")
        self.score = 0
    def scoreupdate(self):
        self.score+=1
        print(f"your score is {self.score}")

    def createsnake(self):

        for segment in self.segment_init_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(segment)
            self.segments.append(new_segment)
    def move(self):
        for segment_positon in range(len(self.segment_init_position) - 1, 0, -1):
            seg_x = self.segments[segment_positon - 1].xcor()
            seg_y = self.segments[segment_positon - 1].ycor()
            self.segments[segment_positon].goto(seg_x, seg_y)
        self.segments[0].forward(20)

        return self.check()
    def Up(self):

        self.segments[0].setheading(90)

    def Down(self):
        self.segments[0].setheading(270)

    def Right(self):
        self.segments[0].setheading(0)

    def Left(self):
        self.segments[0].setheading(180)
    def check(self):
        seg_x = round(self.segments[0].xcor(),0)
        seg_y = round(self.segments[0].ycor(),0)

        self.snakehead = (seg_x,seg_y)
        #print(seg_x,seg_y,self.egg_position)
        if self.egg_position[0] == seg_x and self.egg_position[1] == seg_y :
            print("hit")
            return True
        else:
            False
    def change_egg(self):
        seg_x = random.randrange(0,200,20)
        seg_y = random.randrange(0,200,20)
        self.egg.goto(seg_x,seg_y)
        self.egg_position[0] = seg_x
        self.egg_position[1]=seg_y

    def createegg(self):

        self.egg.color("green")

        self.egg.penup()
        self.egg.goto(100,100)
    def get_position(self):
        self.segment_positions = []
        for segment in self.segments:
            if segment == self.segments[0]:
                continue
            self.segment_positions.append(segment.pos())
        return self.segment_positions
    def Add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        get_position = self.segments[-1].pos()

        new_segment.penup()
        new_segment.goto(get_position[0],get_position[1])
        self.segment_init_position.append(new_segment.pos())

        self.segments.append(new_segment)


