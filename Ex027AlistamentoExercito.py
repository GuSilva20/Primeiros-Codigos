from datetime import date

nome = str(input("Qual seu nome? ")).strip()
print("O Nome inserido é valido? {}".format(nome.isalpha()))
idade = int(input("Ano de Nascimento? "))
ano = int((date.today().year))

if (idade - ano) == 18:
    print("Você esta no periodo do excercito!!")
elif (ano - idade) >= 18:
    print("você está no periodo de alistamento")
    print("Já se passou {} anos do periodo do alistamento".format((ano - idade)-18))
else:
    print("Você ainda não está no Periodo de Alistamento, ainda falta {} anos".format(((ano - idade)-18)))
