from random import randint
from time import sleep
vencedor = True
computador = randint(1, 25)
result = str("")
comp = result
total = 0
while vencedor != False:
    jogador = int(input("Jogue um número: "))
    escolha = str(input("Você quer [PAR/IMPAR]: ")).upper().strip()[0]
    computador = randint(1, 25)
    if total % 2 == 0:
        result = "PAR"
        comp = result.upper().strip()[0]
        total = computador + jogador
    if total % 2 != 0:
        result = "IMPAR"
        comp = result.upper().strip()[0]
        total = computador + jogador
    if escolha == comp:
        vencedor = True
        sleep(1)
        print('Você ganhou, Jogue novamente!')
        print('O computador jogou {} é você {}, o total é {} -> {}'.format(computador, jogador, total, result))
    if escolha != comp:
        vencedor = False
        sleep(1)
        print("Você perdeu")
        print('O computador jogou {} é você {}, o total é {} -> {}'.format(computador, jogador, total, result))
print("fim do programa")
