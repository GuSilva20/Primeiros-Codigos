algo = input('Digite algo: ')
print("O tipo primitivo desse valor é: ", type(algo))

# foi inserido somente espaços?
print('so tem espaços? ',algo.isspace())
print('É um número? ',algo.isnumeric())
print('É Alfabetico? ',algo.isalpha())

# é um número e alfabetico (isalnum)
print('É Alfanúmerico? ',algo.isalnum())
print('Esta em Maiúsculas: ',algo.isupper())
print("Esta em Minusculas? ",algo.islower())

#maiuscula e minuscula (istitle)
print('Esta Capitalizada? ',algo.istitle())
