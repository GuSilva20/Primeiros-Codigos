alt=float(input("Altura da Parede [Metros]: "))
larg=float(input("Largura da Parede [Metros]: "))

area = alt * larg
pintura = area / 2


print("A parede tem {:.2f} de area. \nTinta {:.2f} Litros".format(area,pintura))


#gabarito
alt = float(input("Largura da Parede: "))
larg = float(input("Altura da Parade: "))
area = alt * larg
tinta = area / 2
print('Sua parede tem a dimensao de {} x {} e sua área é de {}'.format(alt,larg,area))
print('para pintar essa parede, você precisará de {} litros de tinta'.format(tinta))
