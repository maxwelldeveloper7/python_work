import car

class ElectricCar(car.Car):
	"""Representa aspectos específicos de veículos elétricos."""
	def __init__(self, make, model, year):
		"""Inicializa os atributos da classe-pai"""
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		"""Exibe uma frase que descreve a capacidade da bateria."""
		print("This car has a " + str(self.battery_size) + "-KWh batte"
		+"ry.")
			
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
