responses = {}

#Define uma flag para indicar que a enquete etá ativa 
polling_active = True

while polling_active:
	#Pede o nome da pessoa e a resposta
	name = input("\nWhat is your name? ")	
	response = input("Which moutain would you like to climb someday? ")
	#Armazena a resposta no dicionário
	responses[name] = response
	#Descobre se outra pessoa vai responser à enquete
	repeat = input("Would you like to let another person respond? "+
	"(yes\no) ")
	if repeat == 'no':
		polling_active = False
		#A enquete foi concluída. Mostra os resultados
		print(responses)
	
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to clim " + response + ".")
