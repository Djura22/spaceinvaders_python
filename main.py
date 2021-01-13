import turtle
import os

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

border_draw = turtle.Turtle()
border_draw.speed(0)
border_draw.color("blue")
border_draw.penup()
border_draw.setposition(-300, -300)
border_draw.pendown()
border_draw.pensize(3)
for side in range(4):
    border_draw.fd(600)
    border_draw.lt(90)
border_draw.hideturtle()

