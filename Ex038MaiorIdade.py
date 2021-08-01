from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input("Ano de Nascimento: "))
    v = (atual - ano)
    print('{} Anos'.format(v))
    if v >= 21:
         maior += 1
    elif v <21:
        menor += 1
    else:
        print("Erro no programa")
print("{} pessoas ja atigiram a  MAIOR IDADE!".format(maior))
print("{} pessoas ainda NÃO ATIGIRAM A MAIOR IDADE".format(menor))



