km = float(input('Qual a velocidade do veiculo? '))

lim = 80

if km <= lim:
    print("O Veiculo não ultrapassou o velocidade!!")

else:
    print("Infelizmente, você ultrapassou o limite de velocidade !!")
    print("Sua Multa sera de R${:.2f} ".format((km - lim) * 7.00))
print('tenha um bom dia, é dirija com cuidado!!!')


