# import colorgram
# colors = colorgram.extract('img.png', 53)
# print(colors)
#
# my_palette = []
# for color in colors:
#     r=color.rgb[0]
#     g=color.rgb[1]
#     b=color.rgb[2]
#     my_palette.append((r,g,b))
# print(my_palette)
from turtle import Turtle, Screen
import random

my_palette = [(125, 100, 57), (186, 168, 100), (165, 150, 59), (52, 49, 42), (90, 93, 108), (127, 148, 181),
              (51, 47, 50), (221, 207, 100), (109, 122, 159), (85, 101, 80), (52, 51, 58), (94, 84, 92), (70, 72, 42),
              (147, 158, 149), (219, 214, 185), (50, 56, 49), (61, 60, 72), (157, 145, 151), (57, 73, 47), (68, 60, 67),
              (191, 208, 221), (116, 138, 109), (82, 57, 49), (199, 210, 202), (158, 116, 103), (140, 119, 128),
              (165, 189, 224), (183, 198, 185), (208, 200, 204), (116, 132, 136), (169, 200, 209), (219, 205, 31),
              (205, 186, 181), (201, 185, 191), (59, 65, 67)]



painta = Turtle()
painta.shape("turtle")
ourscreen = Screen()
ourscreen.colormode(255)
painta.color(random.choice(my_palette))
angle = 0
forward = 0
painta.pensize(13)
painta.speed(2)
painta.penup()
startpos=[-400,-350]


for i in range(1,18):
    startpos[1] += 40
    startpos[0] = -400
    for i in range (1,21):
        painta.setpos(startpos)
        painta.dot(18, random.choice(my_palette))
        startpos[0] += 40


ourscreen.exitonclick()



