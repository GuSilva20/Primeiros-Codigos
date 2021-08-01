#import random
from random import choice, randint, shuffle
n = randint(1, 4)

#resposta --------------------------------------------
al1 = input('Digite o Nome do aluno(a): ')
al2 = input('Digite o Nome do aluno(a): ')
al3 = input('Digite o Nome do aluno(a): ')
al4 = input('Digite o Nome do aluno(a): ')

print('Sequencia de apresentação')
print('--' * 15)
print('1 - {} \n2 - {} \n3 - {} \n4 - {}'.format(al3, al4, al1, al2))

print('O aluno escolhido para apagar o Quadro é: {}'.format(n))


# Gabarito -------------------------------------------------------
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
shuffle(lista)

print('Quem vai apagar o quadro? \nO aluno escolhido foi o {}'.format(escolhido))
print('A Seguencia de tarefas será: ')
print(lista)