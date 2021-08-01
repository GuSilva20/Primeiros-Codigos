nome = str(input("informe seu nome completo: ")).strip()
print("No nome informado tem Silva? {}".format("SILVA" in nome.upper()))

Cid =str(input("Digite o nome da sua Cidade: ")).strip().upper()
Ver = Cid.split()
print("O primeiro nome da cidade informada é Santa? {}".format("SANTA" in Ver[0].upper()))
print(Cid[:5].upper() == "SANTA")


print("O nome {} possui {} letras A.".format(nome, nome.upper().count("A")))
print('A primeira letra A apareceu na posição {}'.format(nome.upper().find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(nome.upper().rfind("A")+1))


Pnome = nome.split()
Un = int(len(nome.split())-1)
print('Primeiro nome: {}'.format(Pnome[0]))
print("ultimo nome: {}".format(Pnome[Un]))