# Space Intruders
# By: Sankhojyoti Halder

import turtle
import random
import winsound

# Setup
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Register shapes
turtle.register_shape("new_invader.gif")
turtle.register_shape("ps_player.gif")
turtle.register_shape("ps_laser1.gif")

# Border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-270, -270)
border.pensize(2)
border.pendown()
for side in range(4):
    border.forward(540)
    border.left(90)
border.hideturtle()

# Create Player
player = turtle.Turtle()
player.color("blue")
player.shape("ps_player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Decide number of enemies
number_of_enemies = 2
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.penup()
    enemy.speed(0)
    enemy.shape("new_invader.gif")
    enemy.color("red")
    enemy.setposition(random.randint(-200, 200), random.randint(100, 250))

enemyspeed = 5


# Create player bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("ps_laser1.gif")
bullet.penup()
bullet.setheading(90)
bullet.speed(0)
bullet.shapesize(.5, .5)
bullet.hideturtle()

bulletspeed = 30


# Move the bullet
bulletstate = "ready"

# Create enemy bullet
ebullet = turtle.Turtle()
ebullet.color("blue")
ebullet.shape("triangle")
ebullet.penup()
ebullet.setheading(270)
ebullet.speed(0)
ebullet.shapesize(.3, .3)
ebullet.hideturtle()

ebulletspeed = 30


# Move the bullet
ebulletstate = "ready"

# Set the score to zero
score = 0

# Score turtle
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.penup()
score_turtle.color("white")
score_turtle.setposition(-260, 250)
score_turtle.hideturtle()
scorestring = "Score : %s " % score
score_turtle.write(scorestring, False, align="left", font=("Arial", 10, "normal"))


# Move the player
def move_left():
    if player.xcor() >= -240:
        player.setx(player.xcor() - playerspeed)


def move_right():
    if player.xcor() <= 240:
        player.setx(player.xcor() + playerspeed)


def fire_bullet():
    # To make change to bulletstate from within a function
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("bullet", winsound.SND_FILENAME)
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()
        bulletstate = "fired"


def fire_ebullet():
    # To make change to bulletstate from within a function
    global ebulletstate
    if ebulletstate == "ready":
        ebullet.setposition(enemy.xcor(), enemy.ycor() - 10)
        ebullet.showturtle()
        ebulletstate = "fired"


def isCollision(t1, t2):
    if (((t1.xcor() - t2.xcor()) ** 2) + ((t1.ycor() - t2.ycor()) ** 2)) ** (0.5) <= 20:
        return True
    else:
        return False


gamestate = "ongoing"

# Key bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while 2 > 1:
    for enemy in enemies:
        enemy.setx(enemy.xcor() + enemyspeed)
        if enemy.xcor() > 240:
            enemyspeed *= -1
            for enemy in enemies:
                if score >= 100:
                    enemy.sety(enemy.ycor() - 40)
                else:
                    enemy.sety(enemy.ycor() - 25)
        if enemy.xcor() < -240:
            enemyspeed *= -1
            for enemy in enemies:
                if score >= 100:
                    enemy.sety(enemy.ycor() - 40)
                else:
                    enemy.sety(enemy.ycor() - 25)
        if isCollision(bullet, enemy):
            bulletstate = "ready"
            bullet.hideturtle()
            bullet.setposition(0, 400)
            # Reset the enemy
            enemy.setposition(random.randint(-200, 200), random.randint(100, 250))
            # Update the score
            score += 10
            scorestring = "Score : %s " % score
            score_turtle.clear()
            score_turtle.write(scorestring, False, align="left", font=("Arial", 10, "normal"))
        if isCollision(player, enemy):
            bullet.hideturtle()
            player.hideturtle()
            print("GAME OVER")
            score_turtle.setposition(-180, 0)
            score_turtle.write("GAME OVER", False, align="left", font=("Arial", 50, "bold"))
            score_turtle.color("grey")
            score_turtle.setposition(-185, 5)
            score_turtle.write("GAME OVER", False, align="left", font=("Arial", 50, "bold"))
            score_turtle.setposition(-185, -40)
            score_turtle.write(scorestring, False, align="left", font=("Arial", 20, "normal"))
            gamestate = "over"
            break
        if isCollision(player, ebullet):
            ebullet.hideturtle()
            player.hideturtle()
            for enemy in enemies:
                enemy.hideturtle()
            bullet.hideturtle()
            score_turtle.setposition(-180, 0)
            score_turtle.write("GAME OVER", False, align="left", font=("Arial", 50, "bold"))
            score_turtle.color("grey")
            score_turtle.setposition(-185, 5)
            score_turtle.write("GAME OVER", False, align="left", font=("Arial", 50, "bold"))
            score_turtle.setposition(-185, -40)
            score_turtle.write(scorestring, False, align="left", font=("Arial", 20, "normal"))
            gamestate = "over"
            break
        fire_ebullet()
    # Move the bullet
    y = int(bullet.ycor())
    y += int(bulletspeed)
    bullet.sety(y)
    if bullet.ycor() >= 260:
        bullet.hideturtle()
        bulletstate = "ready"

    if score < 50:
        ebullet.hideturtle()
    if score >= 50:
        y = int(ebullet.ycor())
        y -= int(ebulletspeed)
        ebullet.sety(y)
        if ebullet.ycor() <= -260:
            ebullet.hideturtle()
            ebulletstate = "ready"
        if gamestate == "over":
            break

turtle.mainloop()
