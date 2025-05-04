list = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', ('n', 'o')],
]

print(list[0][0])  # a
print(list[2][1])  # l
print(list[2][3][1])  # o

for boxes in list:
    for letter in boxes:
        print(letter)