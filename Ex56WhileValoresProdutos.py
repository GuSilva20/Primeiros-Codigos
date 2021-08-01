from time import sleep
resp = "S"
c = tcompra = prodmax = prodmin = 0
nomeprodmin = ""

print("--"*15)
print("L I S T A   DE   C O M P R A S")
print('--'*15)

while resp in "Ss":
    produto = str(input("Produto: ")).strip()
    valor = float(input("Preço: R$"))
    tcompra += valor
    if c == 0:
        nomeprodmin = produto
        prodmin = valor
    if valor < prodmin:
        nomeprodmin = produto
        prodmin = valor
    if valor > 1000:
        prodmax += 1
    c += 1
    resp = str(input("Quer continuar? [S/N]")).upper().strip()[0]
print("--"*20)
print("Finalizando a lista...")
sleep(1)
print('O total da conta foi: R${:.2f}'.format(tcompra))
print("Temos {} produtos custando mais de R$1000.00".format(prodmax))
print("O produto mais barato foi {} que custa R${:.2f}".format(nomeprodmin, prodmin))
print("--"*20)
