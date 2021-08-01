peso = float(input('Digite seu peso: [KG]'))
alt = float(input('Digite a altura: [m]'))

imc = peso / (alt**2)
print("IMC: {:.2f}".format(imc))

if imc < 18.5:
    print("Abaixo do Peso!")
elif imc >= 18.5 and imc <= 25:
    print("Você está no PESO IDEAL!")
elif 25.1 >= imc and imc <= 30:
    print("Você está com SOBREPESO!")
elif imc >= 30.1 and imc <= 40:
    print("Você está OBESO!")
else:
    print('Você está com OBESIDADE MÓRBIDA!')
