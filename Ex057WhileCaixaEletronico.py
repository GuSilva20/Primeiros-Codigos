from time import sleep
print("--"*15)
print("C A I X A    E L E T R O N I C O ")
print("--"*15)
resp = "S"
while resp == "S":
    saque = int(input("Qual valor você quer sacar? R$"))
    resto = saque
    print("{} Cédulas de R$50".format(int(saque / 50)))
    resto = saque % 50
    sleep(1)
    print("{} Cédulas de R$20".format(int(resto / 20)))
    resto = resto % 20
    sleep(1)
    print("{} Cédulas de R$10".format(int(resto / 10)))
    resto = resto % 10
    sleep(1)
    print("{} Cédulas de R$1".format(int(resto / 1)))
    sleep(1)
    print("--"*15)
    sleep(1)
    print("Finalizando saque...")
    sleep(1)
    print("Saque Finalizado!!")
    sleep(1)
    resp = str(input("Deseja fazer outro saque? [S/N]")).upper().strip()[0]
print("Saindo da Conta")
