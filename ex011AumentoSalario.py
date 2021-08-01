nome = input("Nome do Funcionário: ")
cargo = input('Cargo do funcionário: ')
salario = float(input("Salário do Funcionário[R$]: "))
aumento = float(input('de quanto sera o  aumento do colaborador[%]: '))


bon = (salario * aumento)/100
nsalario =float(salario + bon)

print('Colaborador: {}\nCargo: {}\nSalário antigo: {}R$\nAumento {}% \nNovo Salário: {}R$'.format(nome,cargo,salario,aumento,nsalario))

#Gabarito
print("Colaborador: {}\nCargo: {}\nsalario antigo: {}R$\nAumento {}% \nNovo Salário: {}R$".format(nome,cargo,salario,aumento,salario + (salario * aumento)/100))
