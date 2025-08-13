from p5 import *

screen_size = 400


def setup():
    # Put code to run once here
    size(screen_size, screen_size)
    rect_mode(CENTER)


def draw():
    # Put code to run every frame here
    background(255, 255, 255)
    # Add code to draw your face here
    no_stroke()
    fill(94, 181, 213)
    ellipse(200, 220, 210, 210)
    fill(229, 69, 69)
    ellipse(280, 215, 45, 45)
    ellipse(120, 215, 45, 45)
    rect(200, 215, 170, 40)
    fill(0, 0, 0)
    ellipse(160, 215, 30, 30)
    ellipse(240, 215, 30, 30)
    fill(255, 255, 255)
    ellipse(165, 220, 10, 10)
    ellipse(245, 220, 10, 10)

# Keep this to run your code
run()
