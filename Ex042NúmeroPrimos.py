num = int(input("Digite um número: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end="")
        tot += 1
    else:
        print('\033[31m', end="")
    print("{} ".format(c), end="")
print("\n\033[m0 O número {} foi divisível {} vezes".format(num, tot))
if tot == 2:
    print("É por isso ele É PRIMO")
else:
    print('É por isso ele NÃO É PRIMO')
