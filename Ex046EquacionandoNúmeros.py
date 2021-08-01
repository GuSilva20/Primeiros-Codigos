c = 0
n = 0
while c == 0:
    n = 0
    n1 = int(input("Valor 1: "))
    n2 = int(input("Valor 2: "))
    while n == 0:
        print('''Opções:
[ 1 ] - SOMAR
[ 2 ] - MULTIPLICAR
[ 3 ] - MAIOR
[ 4 ] - NOVOS NÚMEROS
[ 5 ] - SAIR DO PROGRAMA''')
        opcao = int(input("Qual opção? "))

        if opcao == 1:
            s = n1 + n2
            print("A SOMA dos Valores {} e {} = {}".format(n1, n2, s))
            n = 0
        elif opcao == 2:
            m = n1 * n2
            print("A MULTIPLICAÇÃO entre os números {} e {} = {}".format(n1, n2, m))
            n = 0
        elif opcao == 3:
            maior = 0
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print("O MAIOR Número é {}".format(maior))
            n = 0
        elif opcao == 4:
            c = 0
            n = 1
        elif opcao == 5:
            print("Saindo do programa!")
            c = 1
            n = 1
        else:
            c = 0
            print("Opção Invalida, tente novamente!")
print("Fim do Programa")

