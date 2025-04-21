# logic operator 'not'
# used to invert expressions
# not True = False
# not False = True

password = input('type the password: ')

if not password == '123456':
    print('access denied')
else:
    print('access granted')
