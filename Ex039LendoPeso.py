maior = 0
menor = 100
for c in range(1,6):
    peso = float(input("Digite o Peso: [kg]"))
    if peso > maior:
        maior = peso
        print("Peso Registrado!")
    elif peso < menor:
        menor = peso
        print("Peso Registrado!")
    else:
        print("Peso Registrado!")
print('MAIOR PESO: {}'.format(maior))
print("MENOR PESO: {} ".format(menor))