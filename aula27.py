from random import randint

'''
repetition
while
exec an action while the condition is true
'''

condition = True

while condition:
    number = randint(1, 10)
    print(f'{number}')
    
    if number == 3:
        break

print("random = find")