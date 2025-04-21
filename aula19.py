'''
basic string interpolation

s - string
d e i - int
f - float
x e X - hexadecimal(ABCDEF0123456789)
'''

name = 'Renato'
age = 30
var = '%s is %d years old' % (name, age)
print(var)  # Renato is 30 years old
print('O hexadecimal de %d é %08X' % (age, age))  # O hexadecimal de 30 é 0000001E

