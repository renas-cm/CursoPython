'''
ask the user to type: name age
if name and age are not empty show:
your name is {name}
seu nome invertido é {name}
your name contains(or not) '' 
your name has {quantity} letters
the first letter is {first letter}
the last letter is {last letter}

if all is empty show: nothing typed
'''

name = input('type your name: ')
age = input('type your age: ')

if name and age:
    print(f'your name is {name}')
    print(f'seu nome invertido é {name[::-1]}')
    if '' in name:
        print(f'your name contains space') 
    else:
        print(f'your name does not contain space')
    print(f'your name has {len(name)} letters')
    print(f'the first letter is {name[0]}')
    print(f'the last letter is {name[-1]}')
else:
    print('nothing typed')