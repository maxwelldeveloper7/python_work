pets = ['dog', 'cat', 'dog', 'golfish', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:
	pets.remove('cat')
	
print(pets)

def describe_pet(animal_type, pet_name):
	"""Exibe informações sobre um animal de estimação"""
	print("\nI have a "  + animal_type + "'s name is "+
		pet_name.title() + ".")

describe_pet('hamister', 'harry')
describe_pet('dog', 'willie')

