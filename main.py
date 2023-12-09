import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
# Create our player
player = Player()
car_manager = CarManager()
level = Scoreboard()
# Move our player
screen.listen()
screen.onkey(player.move_player, key="Up")



game_is_on = True
while game_is_on:
    # Create Cars and move them
    car_manager.create_car()
    car_manager.move_cars()
    # Check if the Turtle collided with the car.
    game_is_on = level.check_collision(car_manager.all_cars, player.position())
    # Check if the Turtle has crossed the finish line
    if player.ycor() > 260:
        player.reset_position()  # Reset the position of the turtle
        level.increase_level()  # Increase the current level.
        car_manager.increase_car_speed()  # Increase the car speed

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
