import turtle #A basic function which is good for small games for providing background 
import os #interaction with the operating system via text commands

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #Stops the window from updating: speeds up the game quite a bit

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Speed of animation needed to be done by turtle module
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #Giving dimensions to the paddle
paddle_a.penup() #Avoids the lines left behind by the paddle when it moves
paddle_a.goto(-350, 0) #Starting position of the paddle

# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) #Since right side of screen hence +350s

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 #d represents delta also known as change which is the triangle in physics
ball.dy = 0.2 #d represents delta also known as change which is the triangle in physics. Every time the ball moves it moves by 2 up and diagonally

# Pen (Score system)
pen = turtle.Turtle() 
pen.speed(0) #Animation speed
pen.shape("square")
pen.color("white")
pen.penup() #No line required when moved
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")) #Starting score will be 0; centre alignment, old school font, font size is normal

# Functions
def paddle_a_up(): #Calling paddle_a_up a function
    y = paddle_a.ycor()
    y += 20 #Since y increases when we go up
    paddle_a.sety(y)

def paddle_a_down(): #Calling paddle_a_down a function
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

# Keyboard bindings
wn.listen() #Tells the function to listen for the keyboard input
wn.onkeypress(paddle_a_up, "w") #When user press lowercase 'w' then it will call the function paddle_a_up and adds 20 to the y coordinate
wn.onkeypress(paddle_a_down, "s") 
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down") #Up and Down represent Up arrow and Down Arrow

# Main game loop
while True:
    wn.update() #Updates the screen every time the loop runs
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx) #Combining everything done in #Function
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (Top y coordinate is +300 and bottom y coordinate is -300)

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290) #Ball is sent back from the border
        ball.dy *= -1 #Reverses ball direction
        os.system("afplay bounce.wav&")
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear() #Without this function, the score is overridden over the previous score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #Curly brackets represent basic printing function
        ball.goto(0, 0) #Send the ball back to centre if flown off screen
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50: #All the defined collisions of the top and bottom of both the paddles
        ball.dx *= -1 
        os.system("afplay bounce.wav&") #Music fil which doesn't work cuz of dual boot
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    