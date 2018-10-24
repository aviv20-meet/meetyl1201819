import turtle

import random
turtle.pensize(10)
#Exercise 1
for i in range(5):
	turtle.hideturtle()
	turtle.pencolor(random.choice(['#37AB65', '#3DF735', '#AD6D70', '#EC2504', '#8C0B90', '#C0E4FF', '#27B502', '#7C60A8', '#CF95D7', '#F6CC1D']))
	turtle.forward(100)
	turtle.left(216)
turtle.showturtle()
turtle.penup()
turtle.forward(150)
turtle.pendown()
turtle.begin_fill()
turtle.pencolor('black')
for i in range(3):
	turtle.forward(50)
	turtle.left(90)
turtle.right(45)
turtle.forward(35.35)
turtle.left(90)
turtle.forward(35.5)
turtle.end_fill()
turtle.reset()
turtle.addshape("download.gif")
turtle.shape("download.gif")
def thing():
	turtle.speed(0)
	turtle.forward(200)
	turtle.right(30)
	turtle.forward(75)
	turtle.right(90)
	turtle.forward(60)
	turtle.penup()
	turtle.setpos(0,0)
	turtle.pendown()
	turtle.right(1)
for i in range(360):
	thing()