import turtle
from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

painta = Turtle()

painta.shape("turtle")
ourscreen = Screen()
ourscreen.colormode(255)
painta.color(random_color())
angle = 0
forward = 0
painta.pensize(13)
turtle.speed(2)

# for i in range (0,100):
#     painta.color(int(random.randint(0, 255)), random.randint(0, 255), random.randint(0, 255))
#     painta.setheading(angle)
#     painta.forward(forward)
#     angle += 45
#     forward = 100
#     if not i % 3 == 0:
#         painta.pendown()
#     else:
#         painta.penup()

# i = 3
# sum_angle = 0
# while True:
#     painta.forward(60)
#     painta.right(360/i)
#     sum_angle += 360/i
#
#     if sum_angle % 360 == 0:
#         i += 1
#         painta.color(int(random.randint(0, 255)), random.randint(0, 255), random.randint(0, 255))

def random_direction():
    angle = random.randint(1, 4) * 90
    return  angle

size=0
painta.fillcolor("violet")
ourscreen.bgcolor("slate grey")
while True:
    painta.forward(50)
    painta.setheading(random_direction())
    painta.pencolor(random_color())
    size += 0.01
    painta.shapesize(size)


ourscreen.exitonclick()

