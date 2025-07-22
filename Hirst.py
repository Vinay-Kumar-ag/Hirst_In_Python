from turtle import Turtle , Screen
import  random

jimmy = Turtle()
screen = Screen()
screen.colormode(255) # as it works on value 0 to 1 , so set it for 255


color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20),(134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
              (14, 98, 70), (232, 176, 165), (160, 142, 158),(54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
              ]


jimmy.penup() # as the cursor does not make the line
jimmy.hideturtle() # it hides the cursor
jimmy.speed("fastest")  # cursor speed increases
x = -250
y = -200
while y < 300:

    jimmy.setposition(x, y)

    for _ in range(10):
        jimmy.dot(20, random.choice(color_list))
        jimmy.forward(50)

    y += 50

screen.exitonclick()
