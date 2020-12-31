#Ping Pong Game

"""
First Player :
    Move up = Press 'a'
    Move down = Press 'z'

Second Player : 
    Move up = Press 'Up' arrow
    Move down = Press 'Down' arrow

"""

import turtle
window = turtle.Screen()
window.title("Pong game by Monisha")
window.bgcolor("black")
window.setup(width=800 , height=600)
window.tracer()
#Score
firstPlayerScore = 0
secondPlayerScore = 0

#First Paddle
first_paddle = turtle.Turtle()
first_paddle.speed(0)
first_paddle.shape("square")
first_paddle.color("white")
first_paddle.shapesize(stretch_wid=5, stretch_len=1)
first_paddle.penup()
first_paddle.goto(-350,0)

#Second Paddle
second_paddle = turtle.Turtle()
second_paddle.speed(0)
second_paddle.shape("square")
second_paddle.color("white")
second_paddle.shapesize(stretch_wid=5,  stretch_len=1)
second_paddle.penup()
second_paddle.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Maximum Score to Win : 5 ", align ="center", font=("Courier",12,"normal"))
pen.goto(0,220)
pen.write("Player A : 0 Player B :0 ", align ="center", font=("Courier",12,"normal"))

#Functions Begins For moving the Paddles
def firstPaddleUp():
    y = first_paddle.ycor()
    y += 20
    first_paddle.sety(y)

def firstPaddleDown():
    y = first_paddle.ycor()
    y -= 20
    first_paddle.sety(y)

def secondPaddleUp():
    y = second_paddle.ycor()
    y += 20
    second_paddle.sety(y)

def secondPaddleDown():
    y = second_paddle.ycor()
    y -= 20
    second_paddle.sety(y)


# Keyboard binding for moving paddless
window.listen()
window.onkeypress(firstPaddleUp,"a")
window.onkeypress(firstPaddleDown,"z")
window.onkeypress(secondPaddleUp,"Up")
window.onkeypress(secondPaddleDown,"Down")

#Main game loop
while True:
    window.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        firstPlayerScore += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write("Maximum Score to Win : 5 ", align="center", font=("Courier", 12, "normal"))
        pen.goto(0, 220)
        pen.write("Maximum Score to Win : 5 - Player A : {} Player B : {} ".format(firstPlayerScore,secondPlayerScore), align="center", font=("Courier", 12, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        secondPlayerScore += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write("Maximum Score to Win : 5 ", align="center", font=("Courier", 12, "normal"))
        pen.goto(0, 220)
        pen.write("Maximum Score to Win : 5 - Player A : {} Player B : {} ".format(firstPlayerScore, secondPlayerScore), align="center",font=("Courier", 12, "normal"))

    #Paddles and the ball collisions
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < second_paddle.ycor() + 50 and ball.ycor() > second_paddle.ycor() - 50):
       ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < first_paddle.ycor() + 50 and ball.ycor() > first_paddle.ycor() - 50):
        ball.dx *= -1

    if (firstPlayerScore == 5 or secondPlayerScore == 5 ):
        pen.clear()
        first_paddle.hideturtle()
        second_paddle.hideturtle()
        ball.hideturtle()
        pen.goto(0,200)
        if firstPlayerScore == 5 :
            pen.write("Congrats Player A Won the Game ", align="center", font=("Courier", 24, "normal"))
        else :
            pen.write("Congrats Player B Won the Game ", align="center", font=("Courier", 24, "normal"))
        window.exitonclick()




