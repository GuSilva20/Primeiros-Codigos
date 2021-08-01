aluno = input('Nome do Aluno: ')
n1=int(input('Primeira Nota: '))
n2=int(input("Segunda Nota: "))
n3=int(input("Terceira Nota: "))
n4=int(input("Quarta Nota: "))

média= (n1++n2+n3+n4) / 4

print('O aluno {} teve a média {}'.format(aluno,média))

#gabarito - Sequencia aritimetica Primeiro o () . / . +
print ("O aluno {} teve a média {}".format(aluno,(n1+n2+n3+n4)/4))
