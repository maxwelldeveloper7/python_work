"""Uma classe que pode ser usada para representar um carro."""

class Car():
	"""Uma tentativa simples de representar um carro."""
	
	def __init__(self, make, model, year):
		"""Inicializa os atributos que descrevem um carro."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		"""Devolve um nome descritivo formatado de modo elegante."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def read_odometer(self):
		"""Exibe uma frase que mostra a milhagem do carro."""
		print("This car has " + str(self.odometer_reading) + " miles" +
			" on it.")
	
	def update_odometer(sefl, mileage):
		"""Define o valor de leitura do hodômetro com o valor
		especificado
		Rejeita alteração se for tentativa de definir um valor menor
		para o hodômetro."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		"""Soma a quantidade especificada ao valor de leitura do 
		hodômetro."""
		self.odometer_reading += miles


"""Um conjunto de classe susado para representar  carros à gasolina e 
elétricos"""

class Battery():
	"""Uma tentativa simples de modelar uma bateria para um carro
	elétrico."""
	
	def __init__(self, battery_size = 60):
		"""Inicializa os atributos da bateria."""
		self.battery_size= battery_size
	
	def describe_battery(self):
		"""Exibe uma frase que descreve a capacidade da bateria."""
		print("This car has a " + str(self.battery_size) + "KWh battery.")
	
	def get_range(self):
		"""Exibe frase sobre a distância que o carro pode percorrer
		com essa bateria."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car ca go approximately " + str(range)
		massage += " miles on a full charge."
		print(message)


class ElectricCar(Car):
	"""Modela aspectos de um carro especificos de veículos elétricos."""
	
	def __init__(self, make, model, year):
		"""Inicializa os atributos da classe-pai.
		Em seguida, inicializa os atributos específicos de um carro
		elétrico."""
		
		super().__init__(make, model, year)
		self.battery = Battery()
