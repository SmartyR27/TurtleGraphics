# MINI PROJECT
#PROJECT - 1 : TURTLE GRAPHICS INITIATION

#IMPORTING MODULES AND LIBRARIES...
import turtle
from random import randint

# CREATE NEW FUNCTION...

def drw_spiral():
    window = turtle.Screen()
    window.bgcolor("BLACK")

    obj = turtle.Turtle() #INITIALIZE TO TURTLE()
    obj.shape("arrow")
    obj.speed(0)

    x = 1
    while x < 400:
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)

        window.colormode(255)
        obj.pencolor(r,g,b)
        obj.forward(50+x)
        obj.right(90.911)
        x = x+1
    window.exitonclick()
drw_spiral()

#END OF CODE..
