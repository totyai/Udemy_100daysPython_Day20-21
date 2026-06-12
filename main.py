from turtle import Screen
from snake import Snake
from score import Score
from food import Food
import time

# TODO - Init

#Moving to class
screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
#snakeBody=[]

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



#TODO - Create scoreboard

#TODO - Detect collision with wall

#TODO - Detect collision with tail


def main():
    game_is_on = True
    #initite the Snake
    snake = Snake()
    #TODO - Create snake food
    food = Food()
    #Create Score
    score = Score()

    screen.listen() # To enable keystroke listening

    #Calling in relevant fucntions from snake class
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
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
        
        # Part to manage teh snake
       # To get a smooth update on the screen
        screen.update()
        snake.move()
        time.sleep(0.1)
        screen.update()
        #screen.exitonclick()
        
        #TODO - Detect collision wiht food
        if snake.head.distance(food) < 15:
            score.pointgained()
            food.gotostart()
            #Dispite the name, the following method increase the size of the snake
            snake.initialization(1,snake.lastBody.pos()[0],snake.lastBody.pos()[1])

        #TODO - Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.gameover("wall")
            game_is_on = False
        
        #TODO - Detect collision with tail
        
    
    #Moving to class
    screen.exitonclick()
    


if __name__ == "__main__":
    main()