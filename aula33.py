'''
show index
'''

list = ['a', 'b', 'c', 'd', 'e']

for letter in list:
    for i in range(len(list)):
         if letter == list[i]:
            print(f'Letter {letter} is at index {i}')
            break
        
    
    