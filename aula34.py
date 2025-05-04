'''
enumerate
'''

list ['luiz', 'andre', 'maria']

for item in enumerate(list):
    print(item)

for index, item in enumerate(list):
    print(index, item)
    
    for tupla in enumerate(list):
        print("tupla")
        for valor in tupla:
            print(f'\t{valor}')