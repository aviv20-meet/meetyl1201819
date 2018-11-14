from turtle import *
import turtle 
import random
turtle.colormode(255)
# class Square(Turtle):
# 	def __init__(self,size):
# 		Turtle.__init__(self)
# 		self.shape("square")
# 		self.shapesize(20)
# 	def random_color(self):
# 			self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
# Square1 = Square(10)
# while(True):
# 	Square1.random_color()
class Rectangle(Turtle):
	def __init__(self,width,hieght):
		Turtle.__init__(self)
		self.setheading(90)
		turtle.register_shape("rectangle",((0,0),(width,0),(width,hieght),(0,hieght)))
		self.shape("rectangle")
		# self.forward(width)
		# self.right(90)
		# self.forward(hieght)
		# self.right(90)
		# self.forward(width)
		# self.right(90)
		# self.forward(hieght)
# c = Rectangle(50,60)
class Square(Rectangle):
	def __init__(self,length):
		Rectangle.__init__(self,length,length)
class Hexagon(Turtle):
	def __init__(self,lenght):
		Turtle.__init__(self)
		self.length = lenght
		self.setheading(90)
		turtle.register_shape("Hexagon",((0,0),(self.length,0),((self.length*0.5)+self.length,self.length),(self.length,2*self.length),(0,2*self.length),(-self.length*0.5,self.length),(0,0)))
		self.shape("Hexagon")
ass = Hexagon(50)
turtle.mainloop()

