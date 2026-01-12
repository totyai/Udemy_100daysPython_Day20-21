from turtle import Turtle, Screen
"""
This file will contain the Snake's appearance and movement 
"""

class Snake:
    def new_snake_body(self, xCoord,yCoord):
        body = Turtle()
        body.color("white")
        body.shape("square")
        body.penup()
        body.goto(xCoord-20,yCoord)
        return body

    def initialization(self):
        self.snakeBody.append(self.new_snake_body(xCoord=10,yCoord=0))
        for _ in range(2):
            bodyLen = len(self.snakeBody)
            lastBody = self.snakeBody[bodyLen-1]
            print(lastBody.pos())
            self.snakeBody.append(self.new_snake_body(xCoord=lastBody.pos()[0],yCoord=lastBody.pos()[1]))


    def move(self):
        self.screen.update()
        self.time.sleep(0.1)
        #Move the snakes
        self.snakeBody[0].fd(20)
        self.snake.snakeBody[0].left(20)

        for bodypart_num in range(len(self.snakeBody)-1,0,-1):
            self.snakeBody[bodypart_num].goto(self.snakeBody[bodypart_num-1].xcor(),self.snakeBody[bodypart_num-1].ycor())



    def __init__(self):
        self.screen = Screen()
        self.screen.setup(height=600,width=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.screen.tracer(0)
        self.snakeBody = []
        self.initialization()

        self.screen.exitonclick()
