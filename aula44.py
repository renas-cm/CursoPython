#isinstance

items = [
    'a', 212, 1.1, True, [1, 2, 3], (1, 2),
    {1, 2}, {'name': 'Renato'}
]
for item in items:
    print(f'Item: {item}, Is it a set? {isinstance(item, set)}')

print("\nItems that are sets:")
for item in items:
    if isinstance(item, set):
        print(f'Set: {item}, Is it a set? {isinstance(item, set)}')

print("\nItems that are numbers (int or float) and their double:")
for item in items:
    if isinstance(item, (int, float)):
        print(f'Number: {item}, Double: {item * 2}')
