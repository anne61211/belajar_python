from p5 import *
from random import randint, seed

# Include global variables here
screen_size = 400

# Draw player function goes here
def draw_player():
    player_on = get(mouse_x, 320).hex
    if player_on == safe.hex:
        text('🤠', mouse_x, 320)
    else:
        text('💥', mouse_x, 320)


# Draw obstacles function goes here
def draw_obstacles():
    seed(1234)
    for i in range(20):
        obstacle_x = randint(0, screen_size)
        obstacle_y = randint(0, screen_size) + frame_count * 10
        obstacle_y = obstacle_y % screen_size
        text('🌵', obstacle_x, obstacle_y)

def setup():
    # Put code to run once here
    size(screen_size, screen_size)
    text_size(40)


def draw():
    # Put code to run every frame here
    global safe
    safe = Color(200, 100, 0)
    background(safe)
    draw_obstacles()
    draw_player()

  
# Keep this to run your code
run()
