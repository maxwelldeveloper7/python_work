lista_convidados = ['Maxwell','Henrique','Leonardo']

lista_convidados[0] = 'Nelzita'

lista_convidados.insert(0,'Admilson')
lista_convidados.insert(3,'Rebeca')
lista_convidados.append('Calebe')


print('Você gostaria de participar do jantar ' + lista_convidados[0]+'?')
print('Você gostaria de participar do jantar ' + lista_convidados[1]+'?')
print('Você gostaria de participar do jantar ' + lista_convidados[2]+'?')

print(lista_convidados)


popped_convidados = lista_convidados.pop()
print('Sinto muito por não convidá-lo(a) '+popped_convidados+'.')
popped_convidados = lista_convidados.pop()
print('Sinto muito por não convidá-lo(a) '+popped_convidados+'.')
popped_convidados = lista_convidados.pop()
print('Sinto muito por não convidá-lo(a) '+popped_convidados+'.')
popped_convidados = lista_convidados.pop()
print('Sinto muito por não convidá-lo(a) '+popped_convidados+'.')

del lista_convidados[0]
del lista_convidados[0]

print(lista_convidados)
print(popped_convidados)
