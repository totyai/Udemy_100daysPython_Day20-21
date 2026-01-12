from turtle import Screen, Turtle
from snake import Snake
import time

# TODO - Init
"""
Moving to class
screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snakeBody=[]
"""

#TODO - Create snake body
"""
Moved to class

def new_snake_body(xCoord,yCoord):
    body = Turtle()
    body.color("white")
    body.shape("square")
    body.penup()
    body.goto(xCoord-20,yCoord)
    snakeBody.append(body)
"""
game_is_on = True

#TODO - Create snake food

#TODO - Detect collision wiht food

#TODO - Create scoreboard

#TODO - Detect collision with wall

#TODO - Detect collision with tail


def main():
    #initite the Snake
    snake = Snake()
    """
    Moving to class

    for _ in range(2):
        bodyLen = len(snakeBody)
        lastBody = snakeBody[bodyLen-1]
        print(lastBody.pos())
        new_snake_body(xCoord=lastBody.pos()[0],yCoord=lastBody.pos()[1])
    
    screen.update()
    """
    while game_is_on:
    #TODO - Move snake
        """
        Moving to class
        self.screen.update()
        self.time.sleep(0.1)
        #Move the snakes
        for bodypart_num in range(len(self.snakeBody)-1,0,-1):
            self.snakeBody[bodypart_num].goto(self.snakeBody[bodypart_num-1].xcor(),self.snakeBody[bodypart_num-1].ycor())
       
        snakeBody[0].fd(20)
        snake.snakeBody[0].left(20)

         """
       # To get a smooth update on the screen
        snake.move()
        
    """
    Moving to class
    screen.exitonclick()
    """

if __name__ == "__main__":
    main()