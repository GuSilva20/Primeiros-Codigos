aluno = str(input('Nome do Aluno: ')).strip()
print("O nome inserido é valido? {}".format(aluno.isalpha()))
nt1 = float(input("Primeira nota: "))
nt2 = float(input("Segunda nota: "))

m = (nt1 + nt2) / 2
print('Sua média é {:.1f}'.format(m))

if m >= 7:
    print('Parabéns você foi Aprovado!')
elif 5 <= m <= 6.9:
    print('Você está de recuperação!')
else:
    print("Infelizmente, você está reprovado!")
