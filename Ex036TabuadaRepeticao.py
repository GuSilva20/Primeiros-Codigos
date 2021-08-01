n = int(input("Qual tabuada deseja ver? "))

for c in range(0, 11):
    print("{} X {} = {}".format(n, c, n*c))
    c += 1

print('Fim do programa')
