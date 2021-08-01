# Validação de Nome
nome = str(input("Primeiro nome: ")).strip()
print("O nome inserido é valido? {}".format(nome.isalpha()))

# Validação de Sobrenome
sobrenome = str(input("Segundo nome: ")).strip()
print("O sobrenome inserio é valido? {}".format(sobrenome.isalpha()))

# Validação de Cargo
cargo = str(input("Cargo : "))
print("O cargo inserio é valido? {} ".format(cargo.isalpha()))

sal = float(input("Salário: "))

a = float(sal * 15) / 100
b = float(sal * 10) / 100

if sal > 1250:
    print('Funcionario: {} {} \nCargo: {} \nSalário {} \nAumento de: 10% \nValor: {} \nNovo Salário: {:.2f}'.format(nome, sobrenome,
                                                                                                                 cargo,
                                                                                                                 sal, b,
                                                                                                                 sal + b))
else:
    print('Funcionario: {} \nCargo: {} \nSalário {} \nAumento de: 15% \nValor: {} \nNovo Salário: {:.2f}'.format(nome,
                                                                                                                 cargo,
                                                                                                                 sal, a,
                                                                                                                 sal + a))

#Gabarito
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora".format(sal, novo))
