a = int(input("Primeiro valor: "))
b = int(input("Segunda valor: "))
c = int(input("Terceiro valor: "))
# Verificando quem é meno
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando Quem é maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O Menor valor digitado foi: {}".format(menor))
print('O Maior valor digitado foi: {}'.format(maior))
