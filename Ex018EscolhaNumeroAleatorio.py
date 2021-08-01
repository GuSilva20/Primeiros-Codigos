from random import randint, choice
from time import  sleep
escolha = int(input('Adivinhe o número de 1 a 5: '))
num =(randint(1, 5))
print('Precessando...')
sleep(3)
if int(escolha) == int(num):
    print("Parabens Você acertou!! \no número escolhido foi {}".format(num))
else:
    print("Infelizment você errou!| \no número escolhido foi {}, \ntente novamente!!".format(num))

#Metodo 2
lista = [1, 2, 3, 4, 5]
aleatorio = (choice(lista))
print("Processando...")
sleep(3)
if int(escolha) == int(aleatorio):
    print("Parabens Você acertou!!")
else:
    print("infelizmente você errou, \nO numero escolhido foi: {}".format(aleatorio))
