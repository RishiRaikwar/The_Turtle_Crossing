import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SHAPES = ["circle", "square", "triangle"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_X = 300


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape(random.choice(SHAPES))
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-240, 250)
            new_car.goto(STARTING_X, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
