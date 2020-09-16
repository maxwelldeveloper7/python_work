prompt = "\nPlease enter ehe name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I' love to go to "+city.title()+"!")
