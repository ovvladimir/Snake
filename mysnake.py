from turtle import Turtle, Screen
import random

SIZE = 40
running = False
dr = [0]
clr = ['red', 'orange', 'purple1', 'red4', 'gold', 'salmon', 'cyan2']

screen = Screen()
screen.delay(0)
screen.title('Змейка')
screen.bgcolor('navy')

line = Turtle()
line.speed(0)
line.width(SIZE)
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
snake.color('red', 'green')

tr = Turtle(shape='arrow')
tr.up()
tr.speed(0)
tr.color('red')

food = Turtle(shape='circle')
food.up()
food.shapesize(1.5, 1.5, 3)
food.speed(0)
food.color('green', 'red')
food.setpos(random.randrange(-360, 400, SIZE),
            random.randrange(-280, 320, SIZE))

text = Turtle()
text.hideturtle()
text.speed(0)
text.pu()
text.setpos(0, 150)
text.color('yellow')

snake.hideturtle()
food.hideturtle()
tr.hideturtle()


def key_up(): dr[0] = 90


def key_down(): dr[0] = 270


def key_right(): dr[0] = 0


def key_left(): dr[0] = 180


def start_snake():
    global running, spd, score
    if not running:
        snake.goto(0, 0)
        spd = 250
        score = 1
        dr[0] = 0
        text.clear()
        text.setpos(-380, 300)
        text.write(f'Score: {score}', align='left', font='arial 14 bold')
        text.setpos(370, 300)
        text.write(f'Speed: {255-spd} km/h', align='right', font='arial 14 bold')
        snake.showturtle()
        food.showturtle()
        tr.showturtle()
        running = True
        main()


def goto_snake(x, y):
    snake.seth(dr[0])
    if dr[0] == 0:
        snake.setx(x+SIZE)
    if dr[0] == 90:
        snake.sety(y+SIZE)
    if dr[0] == 180:
        snake.setx(x-SIZE)
    if dr[0] == 270:
        snake.sety(y-SIZE)
    tr.seth(dr[0])
    tr.setpos(snake.pos())


def goto_tail(n, x1, y1):
    list_snake[n].setpos(x1, y1)


def startgame():
    text.setpos(0, 0)
    text.write("press key 'space' to start the game", align='center',
               font='arial 28 bold')


def main():
    global running, spd, score

    if running:
        for n in range(len(list_snake)-1, 0, -1):
            goto_tail(n, list_snake[n-1].xcor(), list_snake[n-1].ycor())

        goto_snake(snake.xcor(), snake.ycor())

        if snake.distance(food) < 2 or tr.pos() == food.pos():
            food.setposition(random.randrange(-360, 400, SIZE),
                             random.randrange(-280, 320, SIZE))
            food.color('green', clr[random.randint(0, len(clr)-1)])
            score += 1
            spd -= 5
            text.clear()
            text.setpos(-380, 300)
            text.write(f'Score: {score}', align='left', font='arial 14 bold')
            text.setpos(370, 300)
            text.write(f'Speed: {255-spd} km/h', align='right', font='arial 14 bold')

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


screen.onkey(key_up, 'Up')
screen.onkey(key_down, 'Down')
screen.onkey(key_left, 'Left')
screen.onkey(key_right, 'Right')
screen.onkey(start_snake, 'space')
screen.listen()

startgame()
screen.mainloop()
