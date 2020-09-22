"""Devolve um nome completo formatado de modo elegante."""
def get_formatted_name(first_name, last_name, middle_name=''):
	
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name('jimi', 'hendrix')
print(get_formatted_name('maxwell', 'chaves', 'de oliveira'))
print(musician)
