# dict comprehension and set comprehension

produto = {
    'name': 'product1',
    'price': 10,
    'category': 'category1'
}

for key, value in produto.items():
    print(f'{key}: {value}')
    
dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in produto.items()
    # Uncomment the next line to exclude the 'category' key
    # if key != 'category'
}
print(dc)

list = [
    ('a', 'value a'),
    ('b', 'value b'),
    ('a', 'value a'),
]


print(dict(list))

s1 = {2 ** i for i in range(10)}
print(s1)