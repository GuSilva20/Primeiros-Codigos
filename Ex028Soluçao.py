from datetime import date
atual= date.today().year
nascimento = input(input("Ano de Nascimento: "))
idade = atual - nascimento
print("O atleta tem {} anos".format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print("Classificação: SÊNIOR")
elif idade >25.1:
    print("Classificação: MASTER")
else:
    print("--------------")
