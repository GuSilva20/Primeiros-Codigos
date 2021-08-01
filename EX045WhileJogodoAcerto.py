from random import randint
c = 0
toterro = 0
while c == 0:
    v = randint(1, 10)
    n = int(input("Digite um número de 1 a 10: "))
    if n != v:
        print("Você errou!! o número escolhido foi {} Tente Novamente!".format(v))
        toterro = toterro + 1

    if n == v:
        print("Parabéns!!!, Você acertou")
        c = 1

print("Fim do jogo")
print("Você fez {} Tentativas até acerta o número!!!".format(toterro))
