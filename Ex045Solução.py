from random import randint
computador = randint(1, 300)
print("Sou seu Computador...Acabei de pensar em um número entre 0 e 10. ")
print("sera que você consegue adiviniar qual foi? ")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print("Acertou com {} tentativas Parabéns!".format(palpite))

