class Dog():
	
	def __init__(self, name, age):
		"""Inicializa os atributos name e age."""
		self.name = name
		self.age = age
	
	def sit(self):
		"""Simula um cachorro sentado em resposta a um comando."""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""simula um cachorro roalndo em resposta a um comando."""
		print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
