l1 = float(input("Digite a Hipotenusa: "))
l2 = float(input("Digite o Cateto Oposto: "))
l3 = float(input("Digite o Cateto Adjacente: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um TRIÂNGULO!', end="")
    if l1 == l2 == l3:
        print("EQUILATERO!")
    if l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

"""
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l2 + l1):
    print("As Médidas formam um Triangulo")
elif (l1 == l2 and l1 == l3) or (l2 == l3 and l2 == l1):
    print("O triangulo e EQUILATERO")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("O triangulo é ISÓSCELES")
else:
   print("O triangulo é ESCALENO")
  """