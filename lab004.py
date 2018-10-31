class Animal():
	def __init__(self,name,animal_type,fav_food,fav_color,sound):
		self.name = name
		self.type = animal_type
		self.fav_food = fav_food
		self.fav_color = fav_color
		self.sound = sound
	def eat(self):
		print(self.name +" is eating his favorite food"+self.fav_food)
	def description(self):
		print(self.name+" is a "+self.type+" and it's favorite color is "+self.fav_color)
	def make_sound(self):
		num_times = input("Choose the number of times you want the animal too make a sound\n")
		print((self.sound+" ") * int(num_times))
dog = Animal("Buddy","dog","red meat","red","bark")
dog.eat()
dog.description()
dog.make_sound()
class Person():
	def __init__(self,name,age,sport,breakfeast,color):
		self.name = name
		self.age = age
		self.sport = sport
		self.breakfeast = breakfeast
		self.color = color
	def eat_breakfeast(self):
		print(self.name+" is eating "+self.breakfeast+" which is his/hers favorite breakfeast")
	def play_sport(self):
		print(self.name+" is playing his/hers favorite sport, "+self.sport)
joe = Person("joe","45","baseball","mapel syrup","blue")
joe.eat_breakfeast()
joe.play_sport()