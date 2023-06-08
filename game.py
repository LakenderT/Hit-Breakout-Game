import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -280)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Create the bricks
bricks = []
brick_colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    brick = turtle.Turtle()
    brick.shape("square")
    brick.color(brick_colors[i])
    brick.shapesize(stretch_wid=1, stretch_len=5)
    brick.penup()
    brick.goto(-220, 200 - i * 25)
    bricks.append(brick)

# Move the paddle left and right
def move_left():
    x = paddle.xcor()
    if x > -250:
        x -= 20
        paddle.setx(x)

def move_right():
    x = paddle.xcor()
    if x < 250:
        x += 20
        paddle.setx(x)

# Set up the keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Set up the game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collisions with the walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        time.sleep(1)

    # Check for collisions with the paddle
    if ball.ycor() < -270 and ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50:
        ball.dy *= -1

    # Check for collisions with the bricks
    for brick in bricks:
        if ball.distance(brick) < 30:
            bricks.remove(brick)
            brick.hideturtle()
            ball.dy *= -1

    # Check if the player has won
    if len(bricks) == 0:
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
        turtle.write("You win!", align="center", font=("Arial", 24, "normal"))
        break

    # Pause for a moment before the next frame
    time.sleep(0.02)

# Keep the screen open until the user closes it
turtle.done()
