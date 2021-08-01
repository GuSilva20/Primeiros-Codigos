for c in range(1, 5):
    nome: str = str(input("Digite o nome: "))
    sexo = str(input("Sexo[M][F]: "))
    idade = int(input("Idade: "))
    media = 0
    idadehomem = 0
    idademulher = 0
    if sexo.upper() == "M":
        if idade < idadehomem:
            media += idade
        elif idade > idadehomem:
            nomehomem = nome
            idadehomem = idade
            media += idade
    elif sexo.upper() == "F":
        if idade < 20:
            media += idade
        elif idade >= 20:
            idademulher += 1
            media += idade
    else:
        print("Erro")
print("Á Média de idade do grupo é: {}".format(media / 4))
print("O nome do homem mais velho é {} com a idade {} ".format(nomehomem,idadehomem))
print("A quantidade de mulher com mais de 20 anos é {}".format(idademulher))
