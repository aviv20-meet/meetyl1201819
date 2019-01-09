from turtle import Turtle 
import turtle
import random 
import math
turtle.tracer(0)
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
turtle.listen()
class Ball(Turtle):
	def __init__(self,radius,color,speed,dx,dy,x,y,player):
		Turtle.__init__(self)
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
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
		self.player = player
	
	def move(self):
		if(self.player == False):
			oldx = self.xcor()
			oldy = self.ycor()
			newx= oldx + self.dx
			newy = oldy + self.dy
			self.goto(newx,newy)
			if(newx > (SCREEN_WIDTH-self.radius) or newx < -(SCREEN_WIDTH-self.radius)):
				self.dx = self.dx *-1
			if(newy > (SCREEN_HEIGHT-self.radius) or newy < -(SCREEN_HEIGHT-self.radius)):
				self.dy = self.dy *-1


ball = Ball(100,"black",2, 1,2,100,100,True)
ball1 = Ball(100,"green",2,9,7,-100,-100,False)
def movearound(event):
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
		mouse_x = event.x-SCREEN_WIDTH
		mouse_y = SCREEN_HEIGHT-event.y
		dx =  mouse_x - ball.xcor()
		
		dy = mouse_y - ball.ycor() 
		while(math.sqrt(dx**2 + dy **2) > 10):
			dx = dx/2
			dy = dy/2
		print("{0} {1} {2} ".format(ball.xcor(), mouse_x, dx))
		newx = ball.xcor() + dx#(event.x-SCREEN_WIDTH) + dx
		newy = ball.ycor() + dy #(SCREEN_HEIGHT-event.y) + dy
		
		
		if(newx > (SCREEN_WIDTH-ball.radius) or newx < -(SCREEN_WIDTH-ball.radius)):
			ball.dx = ball.dx *-1
		if(newy > (SCREEN_HEIGHT-ball.radius) or newy < -(SCREEN_HEIGHT-ball.radius)):
			ball.dy = ball.dy *-1
		ball.goto(newx,newy)
		ball.dx = dx
		ball.dy = dy

turtle.getcanvas().bind("<Motion>", movearound)
def check_collision(ball1,ball):
	radius_len = ball1.radius + ball.radius
	D = math.sqrt((ball1.xcor()-ball.xcor())**2 + (ball1.ycor()-ball.ycor())**2)
	if(radius_len>D+10):
		return True
	return False
while True:
	if(check_collision(ball,ball1)):
		
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
		'''
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	ball1.move()
	turtle.update()
	ball.move()
	turtle.update()
turtle.mainloop()