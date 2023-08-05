from turtle import  Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)

        self.write(arg=f"score : {self.current_score}",align="center",font=("Arial",24,"normal"))
    def score_update(self):
        self.current_score+=1
        self.clear()
        self.write(arg=f"score : {self.current_score}",align="center",font=("Arial",24,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Gmae Over",align="center",font=("Arial",24,"normal"))




