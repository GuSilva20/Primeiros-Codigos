from random import choice
print("--"*5)
print("Jo Ken Pô")
print("--"*5)

esc = int(input('''
[ 1 ] - Pedra 
[ 2 ] - Papel
[ 3 ] - Tesoura
Escolha: '''))

list = [1, 2, 3]
v = choice(list)

print(v)

if esc == 1 == v:
    print('Empate!')
    elif esc == 1 and

else:
    print("Opção Invalida!")



'''
if esc == "Tesoura" and v == "Papel":
    print("Você {} X {} Computador".format(esc, v))
    print("Parabéns você ganhou!")
elif esc == "Tesoura" and v == "Pedra":
    print("Infelizmente você perdeu!")
    print("Você {} X {} Computador".format(esc, v))
elif esc == "Tesoura" and v == "Tesoura":
    print("Você {} X {} Computador".format(esc, v))
    print("Empate")

elif esc == "Papel" and v == "Tesoura":
    print("Você {} X {} Computador".format(esc, v))
    print("Infelizmente você perdeu!")
elif esc == "Papel" and v == "Pedra":
    print("Você {} X {} Computador".format(esc, v))
    print("Você Ganhou!")
elif esc == "Papel" and v == "Papel":
    print("Empate!")

elif esc == "Pedra" and v == "Tesoura":
    print("Você {} X {} Computador".format(esc, v))
    print("Você ganhou!")
elif esc == "Pedra" and v == "Papel":
    print("Você {} X {} Computador".format(esc, v))
    print('Você Perdeu!')
elif esc == "Pedra" and v == "Pedra":
    print("Empate!")

else:
    print("Erro")
print("Fim de Jogo!")
'''