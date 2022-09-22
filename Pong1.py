# Simple Pong in Python 3

import turtle
import os
import winsound  # sound plays a default sound

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width = 800, height = 600)
wn.tracer(0) # stops the window from updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of the animation
paddle_a.shape('square') # square default is 20 pixels wide and 20 pixels high
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # stretching width by 5 to 100 pixels;
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of the animation
paddle_b.shape('square') # square default is 20 pixels wide and 20 pixels high
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # stretching width by 5 to 100 pixels;
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of the animation
ball.shape('square') # square default is 20 pixels wide and 20 pixels high
ball.color('white')
ball.shapesize(stretch_wid=1, stretch_len=1) # stretching width by 5 to 100 pixels;
ball.penup()
ball.goto(0, 0) # starting point on the screen
ball.dx = 0.1 # ball moves by 0.1 pixels (ball movement speed)
ball.dy = 0.1

# Pen -> used to keep score
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0  Player B: 0', align = 'center', font = ('Courier', 16, 'normal'))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()  # listen to keyboard input
wn.onkeypress(paddle_a_up, 'w')  # when 'w' is pressed, called the function paddle_a_up
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')  # using arrow keys
wn.onkeypress(paddle_b_down, 'Down')


# Main game loop
while True:
    wn.update()  # every time the loop runs, it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= - 1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= - 1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:  # if ball goes off the screen, we put it back into center and reverse the direction
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 16, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 16, 'normal'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
