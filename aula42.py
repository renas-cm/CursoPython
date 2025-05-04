'''
list comprehension
'''

list = [number for number in range(1, 11)]
print(list)

products = [
    {'name': 'product1', 'price': 10},
    {'name': 'product2', 'price': 20},
    {'name': 'product3', 'price': 30},
    {'name': 'product4', 'price': 40},
]

new_products = [
    {'name': product['name'], 'price': product['price'] * 1.05}
    if product['price'] > 20 else {**product}
    for product in products
]

print(*new_products, sep='\n')

list2 = []

for x in range(3):
    for y in range(3):
        list2.append((x, y))
     
     #equal
        
    list2 = [
        (x,y)
        for x in range(3)
        for y in range(3)
    ]
print(list2)

