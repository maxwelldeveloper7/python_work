carro = input("Qual tipo de carro você quer alugar?: ")
print("\nDeixe-me ver se consigo um "+carro.title()+" para você.")

quantidade_pessoas = int(input("Quantas pessoas estão no grupo de"+
	" jantar?: "))

if quantidade_pessoas > 8:
	print("Aguardem uma mesa")
else:
	print("A mesa está pronta")
