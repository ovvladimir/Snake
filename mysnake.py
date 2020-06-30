from turtle import Turtle, Screen
import random

SIZE = 40
score = [1]
spd = [250]
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
snake.hideturtle()

tr = Turtle(shape='arrow')
tr.up()
tr.speed(0)
tr.color('red')
tr.hideturtle()

food = Turtle(shape='circle')
food.up()
food.shapesize(1.5, 1.5, 3)
food.speed(0)
food.color('green', 'red')
food.setpos(random.randrange(-360, 400, SIZE),
            random.randrange(-280, 320, SIZE))
food.hideturtle()

text = Turtle()
text.hideturtle()
text.speed(0)
text.pu()
text.color('yellow')


def key_up():
    dr[0] = 90


def key_down():
    dr[0] = 270


def key_right():
    dr[0] = 0


def key_left():
    dr[0] = 180


def start_snake():
    snake.goto(0, 0)
    spd[0] = 250
    score[0] = 1
    dr[0] = 0
    game_text()
    snake.showturtle()
    food.showturtle()
    tr.showturtle()
    main()


def game_text():
    text.clear()
    text.setpos(-380, 300)
    text.write(f'Score: {score[0]}', align='left', font='arial 14 bold')
    text.setpos(370, 300)
    text.write(f'Speed: {255-spd[0]} km/h', align='right', font='arial 14 bold')


def goto_snake(x, y):
    snake.seth(dr[0])
    if dr[0] == 0:
        snake.setx(x + SIZE)
    if dr[0] == 90:
        snake.sety(y + SIZE)
    if dr[0] == 180:
        snake.setx(x - SIZE)
    if dr[0] == 270:
        snake.sety(y - SIZE)
    tr.seth(dr[0])
    tr.setpos(snake.pos())


def goto_tail(n, x1, y1):
    list_snake[n].setpos(x1, y1)


def startgame():
    text.setpos(0, 0)
    text.write("press key 'space' to start the game", align='center',
               font='arial 28 bold')


def main():
    for n in range(len(list_snake) - 1, 0, -1):
        goto_tail(n, list_snake[n - 1].xcor(), list_snake[n - 1].ycor())

    goto_snake(snake.xcor(), snake.ycor())

    if snake.distance(food) < 2 or tr.pos() == food.pos():
        food.setposition(
            random.randrange(-360, 400, SIZE),
            random.randrange(-280, 320, SIZE))
        food.color('green', clr[random.randint(0, len(clr) - 1)])
        score[0] += 1
        spd[0] -= 5
        game_text()

    if score[0] > len(list_snake):
        tail = list_snake[-1].clone()
        list_snake.append(tail)
        tail.speed(0)

    if snake.xcor() > 360 or snake.xcor() < -360 or \
            snake.ycor() > 280 or snake.ycor() < -280:
        for c in range(1, len(list_snake)):
            list_snake[c].reset()
            list_snake[c].hideturtle()
        del list_snake[1:]
        snake.hideturtle()
        tr.hideturtle()
        food.hideturtle()
        startgame()
        return

    screen.ontimer(main, spd[0])


dct = {
    key_up: 'Up',
    key_down: 'Down',
    key_left: 'Left',
    key_right: 'Right',
    start_snake: 'space'
}
for key, value in dct.items():
    screen.onkey(key, value)
screen.listen()

startgame()
screen.mainloop()
