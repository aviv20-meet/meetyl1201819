from turtle import Turtle 
import turtle
import random 
import math
turtle.tracer(0)
class Ball(Turtle):
	def __init__(self,radius,color,speed,dx,dy,x,y):
		Turtle.__init__(self)
		self.shape('circle')
		self.radius = radius
		self.shapesize(self.radius/10)
		self.color(color)
		self.penup()
		self.speed(0)
		self.dx = dx/10
		self.dy = dy/10
		self.goto(x,y)
		self.speed(speed)
		
	def move(self):
		oldx = self.xcor()
		oldy = self.ycor()
		newx= oldx + self.dx
		newy = oldy + self.dy
		self.goto(newx,newy)
		if(newx > 400 or newx < -400):
			self.dx = self.dx *-1
		if(newy > 400 or newy < -400):
			self.dy = self.dy *-1

ball = Ball(100,"black",2, 8,8,100,100)
ball1 = Ball(100,"green",2,7,9,-100,-100)
def check_collision(ball1,ball):
	radius_len = ball1.radius + ball.radius
	D = math.sqrt((ball1.xcor()-ball.xcor())**2 + (ball1.ycor()-ball.ycor())**2)
	if(radius_len>D):
		return True
	return False
while True:
	if(check_collision(ball,ball1)):
		'''
		ball1.dx = ball1.dx *-1
		ball1.dy = ball1.dy *-1
		ball.dx = ball.dx *-1
		ball.dy = ball.dy *-1
		'''
		tempx = ball1.dx
		tempy = ball1.dy
		ball1.dx = ball.dx
		ball1.dy = ball.dy
		ball.dx = tempx
		ball.dy = tempy
	ball1.move()
	turtle.update()
	ball.move()
	turtle.update()
turtle.mainloop()
