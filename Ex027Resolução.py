from datetime import date
atual = date.today().year

sexo = str(input("Qual seu sexo [M][F}")).upper()
nasc = int(input('Ano Nascimento: '))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
if idade == 18 and sexo == "M":
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18 and sexo == "M":
    saldo = 18 - idade
    print('ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print("Seu alistamento sera em {} anos".format(ano))
elif idade > 18 and sexo == "M":
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    print("Você não precisa se alistar!")
