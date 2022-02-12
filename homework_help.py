import turtle
import random
screen = turtle.Screen()
t = turtle.Turtle()
z = turtle.Turtle()
z.shape("circle")
t.shape("turtle")
z.color("red")
t.color("blue")

# Randomize position of the ball
z.goto(random.randint(-300, 300), random.randint(-300, 300))

# Shoot turtle forwards, then test if turtle is at the ball's location
def move():
    for i in range(300):
        t.forward(1)
        # Change the two numbers to specify the size of the collision box
        if abs(t.xcor() - z.xcor()) < 15 and abs(t.ycor() - z.ycor()) < 15:
            t.write("You Win!")
            turtle.done()
        else:
            continue

# Main Loop
while True:
    t.right(5)
    screen.onkey(move, "space")
    screen.listen()
