M=float(input('Converso de Mentros: '))

#conversão de Medidas
km = M / 1000
hm = M / 100
dam = M / 10
#km = 1
dc = M * 10
cm = M * 100
mm = M * 1000

print('{} Metros Convertidos Corresponde a :\n{} km \n{} Hm \n{} Dam'.format(M,km,hm,dam))
print('{} Dc \n{} Cm \n{} Mm'.format(dc,cm,mm))

#correção
print('{} Metros Convertidos são: \n{} Km \n{} Hm \n{} Dam \n{} Dc \n{} Cm \n{} Mm'.format(M,km,hm,dam,dc,cm,mm))