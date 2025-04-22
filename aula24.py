'''
none = no value
is and is not = identity operators
'''

condition = False
pass_if = None

if condition:
    pass_if = True
    print('The condition is true')
else:
    pass_if = True
    print('The condition is false')

# teste    
print(pass_if, pass_if is None)
print(pass_if, pass_if is not None)

if pass_if is None:
    print('dont pass if')
else:
    print('pass if')