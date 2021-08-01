from random import randint
v = 0
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
# tipo = str(input('Par ou impar? '))
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total de {total} ', end='')
    print('Deu Par'if total % 2 == 0 else 'Deu Impar')
    if tipo == "P":
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print("Você Perdeu!")
            break
    if tipo == "I":
        if total % 2 == 1:
            print("Você venceu!")
            v += 1
        else:
            print("VocÊ Perdeu!")
            break
        print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} Vezes.')