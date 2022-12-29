import time
from turtle import Turtle, Screen
from random import randint
import random as r

# Colors
colors = ['red', 'green', 'yellow', 'orange', 'pink']
segments = []

# initialize score
score = 0

# setup screen
window = Screen()
window.title("SNAKE GAME")
window.bgcolor('black')
window.setup(width=1000, height=780)


# drawing border
def score_board():
    line = Turtle()
    line.pensize(5)
    line.penup()
    line.forward(290)
    line.left(90)
    line.color('white')
    line.pendown()
    line.forward(290)
    line.right(180)
    line.forward(580)
    line.penup()
    line.right(90)
    line.pendown()
    line.forward(580)
    line.right(90)
    line.forward(580)
    line.right(90)
    line.forward(580)
    line.penup()

    line.goto(0, 0)
    line.left(90)
    line.forward(320)
    line.left(90)
    line.forward(50)
    line.pendown()
    line.hideturtle()
    line.penup()


score_board()

# writing score
score_line = Turtle()
score_line.penup()
score_line.speed(0)
score_line.goto(0, 320)
score_line.color('white')
score_line.pendown()
score_line.write("Score:0", align="center", font=("Courier", 20, "normal"))
score_line.hideturtle()

# creating a snake
snake = Turtle()
snake.penup()
snake.shape("square")
snake.color('blue')
snake.goto(0, 0)
snake.direction = 'stop'

# creating a food
food = Turtle()
food.shape('turtle')
food.color('red')
food.speed(0)
food.up()
food.goto(randint(-285, 285), randint(-285, 285))


# Handling keyboard
def move_up():
    if snake.direction != 'down':
        snake.direction = 'up'


def move_down():
    if snake.direction != 'up':
        snake.direction = 'down'


def move_left():
    if snake.direction != 'right':
        snake.direction = 'left'


def move_right():
    if snake.direction != 'left':
        snake.direction = 'right'


def update_score(score):
    return score


# handling directions
window.listen()
window.onkeypress(move_up, 'Up')
window.onkeypress(move_down, 'Down')
window.onkeypress(move_right, 'Right')
window.onkeypress(move_left, 'Left')


# game over
def game_over():
    game_over = Turtle()
    game_over.hideturtle()
    game_over.color('white')
    game_over.write("Game Over!", align="center", font=("Courier", 45, "normal"))

    time.sleep(2)
    game_over.clear()
    snake.goto(0, 0)
    snake.direction = 'stop'

    for seg in segments:
        seg.hideturtle()
    segments.clear()

    global score
    score = 0
    score_line.clear()
    score_line.write(f"Score:{score}", align="center", font=("Courier", 20, "normal"))


while True:

    window.update()

    # shuffling colors
    r.shuffle(colors)

    # detecting collision with borders
    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
        game_over()

    # detecting collision with body
    for segment in segments:
        if snake.distance(segment) < 15:
            game_over()

    # detecting distance between snake and food
    if snake.distance(food) < 20:
        food.goto(randint(-285, 285), randint(-285, 285))
        score += 1
        up_score = update_score(score)

        score_line.clear()
        score_line.write("Score:{}".format(up_score), align="center", font=("Courier", 20, "normal"))

        new_body = Turtle()
        new_body.speed(0)
        new_body.penup()
        new_body.shape('square')
        new_body.color(r.choice(colors))

        segments.append(new_body)

    # reverse segments
    for seg in range(len(segments) - 1, 0, -1):
        segments[seg].goto(segments[seg - 1].xcor(), segments[seg - 1].ycor())

    if len(segments) > 0:
        segments[0].goto(snake.xcor(), snake.ycor())

    # Directions
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)

    time.sleep(0.1)


window.mainloop()
