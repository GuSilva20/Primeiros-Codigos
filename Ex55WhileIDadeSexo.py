from time import sleep
maiores = homens = mulheres = 0
resp = " "
while resp not in "N":
    sexo = " "
    resp = " "
    idade = int(input("Idade: "))
    if idade > 18:
        maiores += 1
    while sexo not in 'MF':
        sexo = str(input("Sexo [M/F]:")).upper().strip()[0]
    if sexo == "M":
        homens += 1
    if sexo == "F":
        if idade < 20:
            mulheres += 1
    while resp not in "SN":
        resp = str(input("Você quer continuar? [S/N]")).upper().strip()[0]
print("Finalizando o Programanda...!!")
sleep(1)
print("Total de pessoas com mais de 18 Anos: {}".format(maiores))
print("Ao todo temos {} Homens cadastrados".format(homens))
print("é temos {} mulheres com menos de 20 anos".format(mulheres))
