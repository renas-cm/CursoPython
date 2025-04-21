'''
String formatting

x or X - hexadecimal (ABCDEF0123456789)
(character)(><^)(quantity)

> - left align
< - right align
^ - center align
= - force the number appear before the number

signal + - or -
ex: 0>-100,.1f
conversion flags - !r, !s, !a
'''

var = "ABC"
var2 = 2205
print(f'{var}') # ABC
print(f'{var:<10}')  # left align
print(f'{var:>10}')  # right align
print(f'{var:^10}')  # center align
print(f'{var:$^10}') # center align with $
print(f'{20507.110807:.1f}') # 20507.1
print(f'{20507.110807:,.1f}') # 20,507.1

print(f'O hexadecimal de {var2} é {var2:08X}') # O hexadecimal de 2205 é 000008AA
