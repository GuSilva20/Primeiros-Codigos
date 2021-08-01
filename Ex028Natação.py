from datetime import date
nasc = float(input("Digite sua data de Nascimento: "))

ano = date.today().year
cat = (ano - nasc)

print('Idade: {}'.format(cat))


if cat <= 9:
    print("Categoria MIRIM")
elif cat >= 9.1 and cat <= 14:
    print('Categoria INFANTIL')
elif 14.1 <= cat and cat <= 19:
    print("Categoria JUNIOR")
elif cat >= 19.1 and cat <= 20:
    print("Categoria SÊNIOR")
else:
    print("Categoria MASTER")
