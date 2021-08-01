nome = str(input("Escreva seu nome completo: ")).strip()
print('Analisando seu nome....')
print("Seu nome em minúsculas é: {}".format(nome.lower()))
print('Seu nome em maiusculas é: {}'.format(nome.upper()))

#Respota Errada
print('Seu nome tem {} letras'.format(len(nome)))
#Gabarito
print('Seu nome tem {} letras'.format(len(nome) - nome.count(" ")))

PNome = nome.split()
#Resposta - Correta
print("O nome {} Possui {} Letras".format(PNome[0], (len(PNome[0]))))
#Gabarito
print("O seu Primeiro nome tem {} letras".format(nome.find(" ")))
