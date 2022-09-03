from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score

screen = Screen()
screen.bgcolor("Black")
screen.setup(800, 600)
screen.tracer(0)
r_paddle = Paddle()
position1 = (350, 0)
r_paddle.create_paddle(position=position1, color="red")
l_paddle = Paddle()
position2 = (-350, 0)
l_paddle.create_paddle(position=position2, color="blue")
score = Score()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

game_on = True
ball = Ball()

while game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move_ball()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.turn()

    # detect collision with paddle:
    if ball.distance(r_paddle) < 60 and 320 < ball.xcor() < 340:
        ball.bounce()

    if ball.distance(l_paddle) < 60 and -340 < ball.xcor() < -320:
        ball.bounce()

    # detect if r_paddle misses:
    if ball.xcor() > 370:
        # ball.clear()
        # ball.goto(0, 0)
        # ball.bounce()
        # ball.move_ball()
        ball.reset_position()
        score.l_point()
        if score.l_score == 5:
            score.game_over(color="Blue")
            game_on = False

    if ball.xcor() < -370:
        ball.reset_position()
        score.r_point()
        if score.r_score == 5:
            score.game_over(color="Red")
            game_on = False

screen.exitonclick()


#program over
