filename = 'pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
	pi_string = ''
	
for line in lines:
	pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
	print("You birthday appears in the million digits of pi!")
else:
	print("You birthday does not appear in the first million digits of"+
	" pi.")
