from math import trunc

nome = str(input("Nome: ")).strip()
casa = float(input("Valor da Casa: R$"))
sal = float(input('Salário: R$'))
pmax = int((sal * 30) / 100)
print('Valor maximo das parcelas: R${:.0f}'.format(pmax))
print('Pacela minima {:.0f} vezes, pagas em {:.0f} anos '.format(casa/pmax, ((casa/pmax)/12)))

anos = int(input('Em quantos anos você quer Parcela? '))
print('você escolheu dividir em {} anos'.format(anos))
if (casa/(anos*12)) <= pmax:
    print('parabéns, Seu emprestimo foi aprovado!!')
else:
    print('infelizmente o emprestivo foi negado!!!')


#Gabarito