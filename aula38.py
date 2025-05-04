'''
dict
'''

person = {
    'name': 'Lucas',
    'age': 25,
}

for info, res in person.items():
    print(info, res)  # name, age
    
person.setdefault('sobrenome', 'Silva')
print(person)  # {'name': 'Lucas', 'age': 25, 'sobrenome': 'Silva'}