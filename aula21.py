'''
cutting str

012345678910
Hello World
-109876543210

cutting [i:f:p] [::]
'''

var = 'Hello World'
print(var[-11]) # H
print(var[0:5]) # Hello
print(len(var)) # 11
print(var[0:len(var)]) # Hello World             
print(var[0:9:4]) # Hoo
print(var[::4]) # Hoo
print(var[::-1]) # dlroW olleH