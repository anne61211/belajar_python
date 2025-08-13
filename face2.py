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
    fill(0, 0, 0) #FACE PURPLE
    ellipse(200, 210, 240, 240)
    fill(187, 153, 202)
    ellipse(260, 220, 120, 200)
    ellipse(140, 220, 120, 200)
    ellipse(200, 280, 200, 120)
    rect(200, 200, 170, 60)
    fill(0, 0, 0) #EYES
    ellipse(150, 215, 30, 30)
    ellipse(250, 215, 30, 30)
    fill(255, 255, 255)#MINI EYES
    ellipse(155, 210, 10, 10)
    ellipse(255, 210, 10, 10)
    fill(187, 153, 202)#PURPLE EYE
    ellipse(150, 235, 30, 30)
    ellipse(250, 235, 30, 30)
    fill(0, 0, 0) #MOUTH
    rect(205, 260, 80, 5)
    triangle(245, 260, 235, 260, 240, 280)
    triangle(175, 260, 165, 260, 170, 280)
    
    

# Keep this to run your code
run()