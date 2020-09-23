"""# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
	'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}

# Resume o pedido
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
	"with following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)"""

def make_pizza(size, *toppings):
	"""Apresenta a pizza que estamos prestes a preparar."""
	print("\nMaking a " + str(size) + 
	"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

