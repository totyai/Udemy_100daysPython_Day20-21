from turtle import Turtle, Screen
import time
"""
This file will contain the Snake's appearance and movement 
"""

#Constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def new_snake_body(self, xCoord,yCoord):
        """Adding new Turtle object"""
        body = Turtle()
        body.color("white")
        body.shape("square")
        body.penup()
        body.goto(xCoord-20,yCoord)
        return body

    def initialization(self,iteration,xCoord,yCoord):
        """Increase snake size"""
        self.snakeBody.append(self.new_snake_body(xCoord,yCoord))
        for _ in range(iteration):
            bodyLen = len(self.snakeBody)
            self.lastBody = self.snakeBody[bodyLen-1]
            #print(self.lastBody.pos())
            self.snakeBody.append(self.new_snake_body(xCoord=self.lastBody.pos()[0],yCoord=self.lastBody.pos()[1]))

    #Changing snake movement
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def move(self):
        #self.screen.update()
        #time.sleep(0.1)
        #Move the snakes
        self.head.forward(MOVE_DISTANCE)
        #self.snake.snakeBody[0].left(MOVE_DISTANCE)

        for bodypart_num in range(len(self.snakeBody)-1,0,-1):
            self.snakeBody[bodypart_num].goto(self.snakeBody[bodypart_num-1].xcor(),self.snakeBody[bodypart_num-1].ycor())



    def __init__(self):
        """
        self.screen = Screen()
        self.screen.setup(height=600,width=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.screen.tracer(0)
        """
        self.snakeBody = []
        self.initialization(iteration=2,xCoord=10,yCoord=0)
        self.head = self.snakeBody[0]

        #self.screen.exitonclick() # - TODO Issue is here. While the creation is correct, it never escaptes from this step forward to the move
