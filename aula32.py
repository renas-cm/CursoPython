'''
changing list
'''

list = [1, 2, 3, 11, 4, 5, 10]
list2 = [14, 15, 16]

del list[0]
print(list)

list.append(17)
print(list)

list.insert(1 , 'Renato')
print(list)

list.pop(1)
print(list)

list.sort()
print(list)

list.extend(list2)
print(list)