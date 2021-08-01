from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input("Em que ano a pessoa nasce?"))
    idade = atual - nasc
    print("Essa pessoa tem {} Anos".format(idade))
    if idade >= 21:
        print("Ela é de MAIOR")
        totmaior += 1
    else:
        print("Ela é de MENOR")
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print("Ao todo tivemos {} pessoas menores de idade".format(totmenor))