# import colorgram
import turtle as t
import random

# colors = colorgram.extract("images.jpg", 30)
# colors_list = []
# for color in colors:
#     r = color.rgb.r 
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     colors_list.append(new_color)

color_list = [(248, 231, 27), (202, 12, 30), (35, 91, 186), (232, 229, 4), (232, 149, 48), (197, 68, 22), (212, 13, 9), (35, 31, 152), (49, 220, 60), (241, 46, 151), (20, 22, 53), (14, 208, 224), (75, 9, 53), (17, 154, 18), (55, 26, 13), (80, 193, 223), (219, 23, 116), (232, 159, 8), (241, 64, 24), (221, 138, 191), (96, 75, 10), (247, 11, 9), (83, 238, 162), (11, 96, 63), (5, 35, 33), (89, 208, 147)]

new_tur = t.Turtle()
new_tur.penup()
new_tur.hideturtle()
t.colormode(255)
new_tur.speed("fastest")

new_tur.setheading(225)
new_tur.forward(300)
new_tur.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    new_tur.dot(20, random.choice(color_list))
    new_tur.forward(50)

    if dot_count % 10 == 0:
        new_tur.setheading(90)
        new_tur.forward(50)
        new_tur.setheading(180)
        new_tur.forward(500)
        new_tur.setheading(0)


myscreen = t.Screen()
myscreen.exitonclick()

