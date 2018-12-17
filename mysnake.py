from turtle import Turtle, Screen
import random

size = 40
running = False

screen = Screen()
screen.delay(0)
screen.title('Змейка')
screen.bgcolor('navy')

line = Turtle()
line.speed(0)
line.width(size)
line.pencolor('blue')
line.up()
line.setpos(-380, 320)
line.down()
line.setpos(380, 320)
line.up()
line.setpos(-380, -320)
line.down()
line.setpos(380, -320)
line.hideturtle()

snake = Turtle(shape='square')
list_snake = [snake]
snake.speed(0)
snake.up()
snake.shapesize(2)
snake.color('green')
snake.pencolor('red')

tr = Turtle(shape='arrow')
tr.up()
tr.speed(0)
tr.color('red')

food = Turtle(shape='circle')
food.up()
food.shapesize(1.5, 1.5, 3)
food.speed(0)
food.color('red')
food.pencolor('green')
food.setpos(random.randrange(-360, 400, size),
            random.randrange(-280, 320, size))

text = Turtle()
text.hideturtle()
text.speed(0)
text.pu()
text.setpos(0, 150)
text.color("yellow")

snake.hideturtle()
food.hideturtle()
tr.hideturtle()


def u():
    global dr
    dr = 90


def d():
    global dr
    dr = 270


def r():
    global dr
    dr = 0


def l():
    global dr
    dr = 180


def sp():
    global running, spd, score, dr
    if not running:
        snake.goto(0, 0)
        spd = 250
        score = 1
        dr = 0
        text.clear()
        text.setpos(-380, 300)
        text.write("Score: " + str(score), align="left",
                   font=("Arial", 14, 'bold'))
        text.setpos(370, 300)
        text.write(f"Speed: {str(255-spd)} km/h", align="right",
                   font=("Arial", 14, 'bold'))
        snake.showturtle()
        food.showturtle()
        tr.showturtle()
        running = True
        main()


def goto_snake(x, y):
    snake.seth(dr)
    if dr == 0:
        snake.setx(x+size)
    if dr == 90:
        snake.sety(y+size)
    if dr == 180:
        snake.setx(x-size)
    if dr == 270:
        snake.sety(y-size)
    tr.seth(dr)
    tr.setpos(snake.pos())


def goto_tail(x1, y1):
    list_snake[n].setpos(x1, y1)


def startgame():
    if not running:
        text.setpos(0, 0)
        text.write("press key 'space' to start the game", align="center",
                   font=("Arial", 28, 'bold'))


def main():
    global score, spd, n, running

    if running:
        for n in range(len(list_snake)-1, 0, -1):
            goto_tail(list_snake[n-1].xcor(), list_snake[n-1].ycor())

        goto_snake(snake.xcor(), snake.ycor())

        if snake.distance(food) < 2 or tr.pos() == food.pos():
            food.setposition(random.randrange(-360, 400, size),
                             random.randrange(-280, 320, size))
            score += 1
            spd -= 5
            text.clear()
            text.setpos(-380, 300)
            text.write("Score: " + str(score), align="left",
                       font=("Arial", 14, 'bold'))
            text.setpos(370, 300)
            text.write(f"Speed: {str(255-spd)} km/h", align="right",
                       font=("Arial", 14, 'bold'))

        if score > len(list_snake):
            tail = list_snake[-1].clone()
            list_snake.append(tail)
            tail.speed(0)

        if (snake.xcor() > 360 or snake.xcor() < -360 or
                snake.ycor() > 280 or snake.ycor() < -280):
            running = False
            for c in range(1, len(list_snake)):
                list_snake[c].reset()
                list_snake[c].hideturtle()
            del list_snake[1:]
            snake.hideturtle()
            tr.hideturtle()
            food.hideturtle()
            startgame()

        screen.ontimer(main, spd)


screen.onkey(u, 'Up')
screen.onkey(d, 'Down')
screen.onkey(l, 'Left')
screen.onkey(r, 'Right')
screen.onkey(sp, 'space')
screen.listen()

startgame()
screen.mainloop()
