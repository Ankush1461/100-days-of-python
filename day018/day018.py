# Hirst Dot Painting Program

## For the list of rgb_colors from image.jpg
# import colorgram as clr
# rgb_colors = []
# colors = clr.extract('image.jpg', 110)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

from turtle import Turtle, Screen, colormode
import random
colormode(255)
tim = Turtle()
rgb_colors = [(230, 225, 219), (219, 230, 221), (234, 222, 228), (221, 225, 233), (228, 208, 98), (218, 150, 101),
              (127, 165, 185), (133, 176, 147), (44, 109, 152), (48, 123, 60), (179, 66, 42), (226, 84, 55),
              (152, 17, 26), (16, 60, 35), (184, 182, 25), (16, 95, 38), (147, 71, 84), (14, 41, 73), (168, 20, 14),
              (237, 205, 7), (49, 21, 16), (80, 15, 21), (186, 140, 149), (216, 68, 78), (64, 162, 83), (233, 170, 162),
              (14, 61, 130), (171, 206, 175), (58, 150, 182), (229, 169, 174), (89, 128, 172), (163, 203, 212),
              (175, 192, 212), (253, 8, 23), (36, 73, 88), (250, 12, 12)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 110
tim.speed("fastest")

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
