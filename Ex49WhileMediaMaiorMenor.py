media = 0
maior = menor = 0
c = 0
r = "S"
while r == "S":
    n = int(input("Digite um número: "))
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    media += n
    c += 1
    r = str(input('Você quer continuar? [ S / N ]')).upper()
print('Finalizando programa!')
print("Média: {}".format(media/c))
print("Maior: {}".format(maior))
print("Menor: {}".format(menor))
