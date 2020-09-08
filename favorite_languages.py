favorite_languages = {
	'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',
}

friends = ['phil', 'sarah']

#exibe valores e chaves
for name, language in favorite_languages.items():
	
	print(name.title())
	
	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite"+
		" language is " + favorite_languages[name].title() + "!")

#exibe nomes ordenados
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")

#exibe apenas os valores
for language in favorite_languages.values():
	print(language.title())

for language in set(favorite_languages.values()):
	print(language.title())
