from turtle import Turtle 
import turtle
import random 
class Ball(Turtle):
	def __init__(self,radius,color,speed,dx,dy):
		Turtle.__init__(self)
		self.shape('circle')

		
		self.radius = radius
		self.shapesize(self.radius/10)
		self.color(color)
		self.speed(speed)
		self.dx = dx
		self.dy = dy 
		
	def move(self):
		oldx = self.xcor()
		oldy = self.ycor()
		newx= oldx + self.dx
		newy = oldy + self.dy
		if(newx>400 or newx < -400):
			self.dx = self.dx *-1
		if(newy >400 or newy < 400):
			self.dy = self.dy *-1

ball = Ball(10,"black",2, 10,3)
ball1 = Ball(10,"green",2,10,7)
def check_collision(ball1,ball2):
	radius_len = ball1.radius + ball2.radius
	D = ((ball1.xcor()-ball2.xcor())**2 + (ball1.ycor()-ball2.ycor())**2)**0.5
	if(radius_len>D):
		return True
	return False
while True:
	ball1.move()
	ball.move()
	collision = check_collision(ball,ball1)
	if(collision == True):
		ball1.dx = ball1.dx *-1
		ball1.dy = ball1.dy *-1
		ball.dx = ball.dx *-1
		ball.dy = ball.dy *-1
turtle.mainloop()