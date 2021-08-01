c = 0
while c == 0:
    sexo = str(input("Digite seu Sexo: [M/F]")).upper()
    if sexo == "M":
        print('O Sexo informado é MASCULINO!')
        c = 1
    if sexo == "F":
        print("O sexo informado é FEMININO!")
        c = 1
print("Programa Finalizado")
