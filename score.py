from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(-10,260)
        self.writescore()

    def writescore(self):
        """This method is used for abstracting the write function"""
        self.write(f"Score: {self.points}", move=False,align="left",font=("Arial", 18, "normal"))

    def pointgained(self):
        """This is a method to be called when the snake hit the food and point is gained."""
        self.clear()
        self.points += 1
        self.writescore()

    def gameover(self, obj):
        self.goto(0,0)
        self.write(f"You have hit the {obj}, game over!", move=False, align="center", font=("Arial", 24, "normal"))