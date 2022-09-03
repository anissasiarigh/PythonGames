from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def game_over(self, color):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over. {color} Wins!!", True,  align="center", font=("JetBrains Mono", 25, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, True, align="center", font=("Jetbrains Mono", 24, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, True, align="center", font=("Jetbrains Mono", 24, "normal"))

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()