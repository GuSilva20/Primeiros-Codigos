print("TABUADA")
tab = int(input("Qual tabuada você quer ver? "))
print("__"*10)
mult = 0
while tab > 0:
    for c in range(1, 11):
        mult = tab * c
        print("{} X {} = {}".format(tab, c, mult))
        c += 1
    print("__"*10)
    tab = int(input("Qual Tabuada você quer ver? "))
    print('--'*10)
print("Finalizando Programa")
