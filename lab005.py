
import tkinter as tk
from tkinter import simpledialog
#Then when ever you want to ask the user for input use this code
def prob1():
	greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
	if greeting in ["Arrr!"]:
		print("Go away, pirate.")
	else:
		print("Greetings, hater of pirates!")
def prob2():
	# A time traveler has suddenly appeared in your classroom!
	# Create a variable representing the traveler's
	# year of origin (e.g., year = 2000)
	# and greet our strange visitor with a different message
	# if he is from the distant past (before 1900),
	# the present era (1900-2020) or from the far future (beyond 2020).
	year = simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw())

	if int(year) <= 1900:
	    print ("Woah, that's the past!")
	elif (int(year) > 1900 and int(year) < 2020):
	    print ("That's totally the present!")
	else:
	    print ("Far out, that's the future!!")
def prob3():
	# Write a simple class that defines a person
	# with attributes of first_name, last_name
	# and has a method signature of "speak" which
	# prints the object as "Jefferson, Thomas".

	class Person():
	  def __init__(self, first_name, last_name):
	    self.first = first_name
	    self.last = last_name
	  def speak(self):
	  	print("My name is "+ self.first + " " + self.last)

	me = Person("Brandon", "Walsh")
	you = Person("Ethan", "Reed")

	me.speak()
	you.speak()
def prob4():

	# Calculating Grades (ok, let me think about this one)

	# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

	# Average	Grade
	# 90+	A
	# 80-89	B
	# 70-79	C
	# 60-69	D
	# 0-59	F

	# Exams: 89, 90, 90
	# Average: 90
	# Grade: A
	# Student is passing.

	# Exams: 50, 51, 0
	# Average: 33
	# Grade: F
	# Student iis failing.

	exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

	exam_two = int(simpledialog.askstring("Input","Input exam grade two: ", parent=tk.Tk().withdraw()))

	exam_three = int(simpledialog.askstring("Input", "Input exam grade three: ", parent=tk.Tk().withdraw()))

	grades = [exam_one, exam_two, exam_three]
	sum = 0
	for grade in grades:
		sum = sum + grade
		avg = sum / len(grades)

	if avg >= 90:
	    letter_grade = "A"
	elif avg >= 80 and avg < 90:
	    letter_grade = "B"
	elif avg > 69 and avg < 80:
	    letter_grade = "C"
	elif avg <= 69 and avg >= 65:
	    letter_grade = "D"
	else:
	    letter_grade = "F"

	for grade in grades:
	    print("Exam: " + str(grade))

	    print("Average: " + str(avg))

	    print("Grade: " + letter_grade)

	if letter_grade is "F":
	    print ("Student is failing.")
	else:
	    print ("Student is passing.")
def prob6():
	class Bear():
		def __init__(self, name):
			self.name = name
			print("A new bear created. Its name is: " + self.name)
		
		def say_hi(self):
			print("Hi! I’m a bear. My name is " + self.name)
	my_bear = Bear("Danny")
	print(my_bear.say_hi())
def prob7():
	balloons = 5
	name = "Ron"
	color = "Yellow"
	print("This is a tale about " + str(balloons) + " balloons. The first kid is " + name + " who got a "+ color + " balloon")
def probb8():
	class Cake():
			def __init__(self,flavor):
				self.cake_flavor = flavor

			def eat(self):
				print("Yummy!!! Eating a "+ self.cake_flavor+" cake :)")

	cake = Cake("chocolate")
	print(cake.eat())
def prob9():
	class Cat():
		def __init__(self, name):
			self.name = name
			self.age = 0 
		def birthday(self,age):
			self.age += 1
			if self.age >= 100:
				print("Dong dong, the cat is dead!")
			else:
				print(self.name, "hasing its", self.age, 'birthday!')

	my_cat = Cat("Salem")
	my_cat.birthday(8)
prob9()
# what I want: my cat to celebrate its 8th birthday (and all the 
# birthdays that come before that)

