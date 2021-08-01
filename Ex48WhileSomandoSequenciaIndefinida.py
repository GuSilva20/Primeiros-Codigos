digitados = 0
soma = 0
n = 0
while n != 999:
    n = int(input("Digite um número: [999 para parar] "))
    if n != 999:
        digitados += 1
        soma += n
print("Programa finalizado")
print("A quantidade de números digitados foi {} e a media deles e {}".format(digitados, soma))
