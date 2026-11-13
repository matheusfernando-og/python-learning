item = input('Digite algo: ')

print('O tipo primitivo desse valor é {0}'.format(type(item)))

print('Só tem espaços? {0}'.format(item.isspace()))
print('É um número? {0}'.format(item.isnumeric()))
print('É alfabético? {0}'.format(item.isalpha()))
print('É alfanumérico? {0}'.format(item.isalnum()))
print('Está em maiúsculas? {0}'.format(item.isupper()))
print('Está em minúsculas? {0}'.format(item.islower()))
print('Está capitalizada? {0}'.format(item.istitle()))