from turtle import Turtle 
import turtle
import random 
import math
turtle.tracer(0)
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
colors = ["Black","Red","Green","Orange","Yellow"]
turtle.listen()
BALLS = []
score = 0
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
def bigger_radius(ball1, ball, num = 1):
	if( num ==1):
		if(ball1.radius > ball.radius):
			return ball1
		if(ball.radius > ball1.radius):
			return ball
		else:
			return ball
	if(num == 2):
		if(ball1.radius < ball.radius):
			return ball1
		if(ball.radius < ball1.radius):
			return ball
		else:
			return ball1
def make_balls():
	global BALLS

	for i in range(1,5):
		color = random.choice(colors)
		x = random.randint(int(-SCREEN_WIDTH),int(SCREEN_WIDTH))
		y = random.randint(int(-SCREEN_HEIGHT),int(SCREEN_HEIGHT))
		dx = random.randint(1,10)
		dy = random.randint(1,10)
		speed = random.randint(1,10)
		radius = random.randint(50,100)
		player = False
		ball = Ball(radius,color,speed, dx,dy,x,y,player)
		BALLS.append(ball)
BALL = Ball(random.randint(60,100),"black",2, 9,9,100,100,True)
# print(BALL.radius)
# print(BALL)
def movearound(event):
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	mouse_x = event.x-SCREEN_WIDTH
	mouse_y = SCREEN_HEIGHT-event.y
	dx =  mouse_x - BALL.xcor()
	
	dy = mouse_y - BALL.ycor() 
	while(math.sqrt(dx**2 + dy **2) > 10):
		dx = dx/2
		dy = dy/2
	print("{0} {1} {2} ".format(BALL.xcor(), mouse_x, dx))
	newx = BALL.xcor() + dx#(event.x-SCREEN_WIDTH) + dx
	newy = BALL.ycor() + dy #(SCREEN_HEIGHT-event.y) + dy
	
	
	if(newx > (SCREEN_WIDTH-BALL.radius) or newx < -(SCREEN_WIDTH-BALL.radius)):
		BALL.dx = BALL.dx *-1
	if(newy > (SCREEN_HEIGHT-BALL.radius) or newy < -(SCREEN_HEIGHT-BALL.radius)):
		BALL.dy = BALL.dy *-1
	BALL.goto(newx,newy)
	BALL.dx = dx
	BALL.dy = dy

turtle.getcanvas().bind("<Motion>", movearound)
def check_collision(ball1,ball):
	if(ball1 != ball):
		radius_len = ball1.radius + ball.radius
		D = math.sqrt((ball1.xcor()-ball.xcor())**2 + (ball1.ycor()-ball.ycor())**2)
		if(radius_len>D+10):
			return True
	return False
def check_all_balls_collision():
	for a_ball in BALLS:
		for b_ball in BALLS:
			if(check_collision(a_ball,b_ball)):
				a_ball_radius = a_ball.radius
				b_ball_radius = b_ball.radius
				color = random.choice(colors)
				x = random.randint(int(-SCREEN_WIDTH),int(SCREEN_WIDTH))
				y = random.randint(int(-SCREEN_HEIGHT),int(SCREEN_HEIGHT))
				dx = random.randint(1,10)
				dy = random.randint(1,10)
				speed = random.randint(1,10)
				radius = random.randint(50,100)
				b = bigger_radius(a_ball , b_ball)
				b1 =  bigger_radius(a_ball , b_ball,2)
				b.x = x
				b.y = y
				b.dx = dx
				b.dy = dy
				b.speed = speed
				b.radius = radius
				b1.radius += 1
				b1.shapesize(b1.radius/10)
				b.goto(x,y)
def check_my_ball_collision():
	global score
	for ball1 in BALLS:
		if(check_collision(BALL,ball1)):
			ball_radius = BALL.radius
			ball1_radius = ball1.radius
			if(bigger_radius(BALL,ball1) == ball1):
				print(BALL)
				print(BALL.radius)
				print(ball1.radius)
				print("\n")
				return False
			color = random.choice(colors)
			x = random.randint(int(-SCREEN_WIDTH),int(SCREEN_WIDTH))
			y = random.randint(int(-SCREEN_HEIGHT),int(SCREEN_HEIGHT))
			dx = random.randint(1,10)
			dy = random.randint(1,10)
			speed = random.randint(1,10)
			radius = random.randint(50,100)
			b = bigger_radius(BALL , ball1 ,2)
			b1 =  bigger_radius(BALL , ball1)
			b.x = x
			b.y = y
			b.dx = dx
			b.dy = dy
			b.speed = speed
			b.radius = radius
			b1.radius += 1
			b1.shapesize(b1.radius/10)
			score +=1
	return True


make_balls()
while check_my_ball_collision() and score < 500:

	check_all_balls_collision()
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	for i in BALLS:
		i.move()
		turtle.update()
print(score)
turtle.mainloop()
