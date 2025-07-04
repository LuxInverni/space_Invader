import turtle
from turtle import Turtle

wn = turtle.Screen()  # wn = window
wn.title('Space Invaders by @LucyWinters')
wn.bgcolor('black')
wn.setup(width=800, height=800)
wn.tracer(0)


# Pen
Player_lives = 1
Aliens_left = 1
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 340)
pen.write("Player 1 lives: {} Aliens Left: {}".format(Player_lives, Aliens_left), align='center', font=("Courier", 24, 'normal'))

# Player Space Ship
Player_Spaceship = turtle.Turtle()
Player_Spaceship.speed(0)  # sets the speed to maximum possible speed in turtle
Player_Spaceship.shape('square')
Player_Spaceship.color('white')
Player_Spaceship.shapesize(stretch_wid=3, stretch_len=1)
Player_Spaceship.penup()
Player_Spaceship.goto(0, -200)

# Alien Spaceship
Alien_Spaceship = turtle.Turtle()
Alien_Spaceship.speed(0)  # sets the speed to maximum possible speed in turtle
Alien_Spaceship.shape('square')
Alien_Spaceship.color('green')
Alien_Spaceship.shapesize(stretch_wid=3, stretch_len=1)
Alien_Spaceship.penup()
Alien_Spaceship.goto(0, 350)
Alien_Spaceship.dx = 4


#Player Projectile
Player_Projectile: Turtle = turtle.Turtle()
Player_Projectile.speed(0)  # sets the speed to maximum possible speed in turtle
Player_Projectile.shape('arrow')
Player_Projectile.color('yellow')
Player_Projectile.setheading(90)
Player_Projectile.penup()
Player_Projectile.dy = 4
projectile_state = 'ready'

# Function
def aliens_down():
    y = Alien_Spaceship.ycor()  # ycor from turtle module returns y coordinates
    y += -40
    Alien_Spaceship.sety(y)

def player_right():
    x = Player_Spaceship.xcor()  # xcor from turtle module returns x coordinates
    x += 40
    Player_Spaceship.setx(x)


def player_left():
    x = Player_Spaceship.xcor()  # xcor from turtle module returns x coordinates
    x += -40
    Player_Spaceship.setx(x)

def player_fire():
    global projectile_state
    if projectile_state == 'ready':
        projectile_state = 'fired'
        x = Player_Spaceship.xcor()
        y = Player_Spaceship.ycor() + 40
        Player_Projectile.setposition(x, y)
        Player_Projectile.showturtle()

# keyboard binding
wn.listen()  # turtle method to listen to keyboard typings
wn.onkeypress(player_right, 'd')
wn.onkeypress(player_left, 'a')
wn.onkeypress(player_fire, 'w')

# Main game loop
while True:
    wn.update()

    # Move the Player Projectile
    Player_Projectile.sety(Player_Projectile.ycor() + Player_Projectile.dy)
    if Player_Projectile.ycor() > 400:
        projectile_state = 'ready'

    # Move the Alien and reverse Alien movement
    Alien_Spaceship.setx(Alien_Spaceship.xcor() + Alien_Spaceship.dx)
    if Alien_Spaceship.xcor() > 300 or Alien_Spaceship.xcor() < -300:
        Alien_Spaceship.dx *= -1  # reverses the direction
        aliens_down()

    #Projectile hits Alien
    if projectile_state == 'fired':
        if (Player_Projectile.ycor() >= Alien_Spaceship.ycor() - 20) and (Player_Projectile.ycor() <= Alien_Spaceship.ycor() + 20):
            if (Player_Projectile.xcor() + 20 >= Alien_Spaceship.xcor()) and (Player_Projectile.xcor() - 20 <= Alien_Spaceship.xcor()):
                Alien_Spaceship.setposition(-600, -800)
                Aliens_left = Aliens_left - 1
                Player_Projectile.hideturtle()
                Alien_Spaceship.hideturtle()
                pen.clear()
                pen.write("Player 1 lives: {} Aliens Left: {}".format(Player_lives, Aliens_left), align='center', font=("Courier", 24, 'normal'))

    #Game Losing Condition: Ship Colision
    if (Alien_Spaceship.ycor() < -200) and not (Alien_Spaceship.ycor() < -500):
        pen.clear()
        pen.write("The Aliens Have Defeated You! Loser!".format(Player_lives, Aliens_left), align='center', font=("Courier", 24, 'normal'))

    # Game Winning Condition
    if Aliens_left == 0:
        pen.clear()
        pen.write("You have defeated the aliens!".format(Player_lives, Aliens_left), align='center', font=("Courier", 24, 'normal'))
