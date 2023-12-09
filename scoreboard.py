from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", False, "left", FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "left", FONT)

    def check_collision(self, all_cars, player_pos):
        for item in all_cars:
            if item.distance(player_pos) < 25:
                self.goto(0, 0)
                self.write("GAME OVER", False, "center", FONT)
                return False
        return True
