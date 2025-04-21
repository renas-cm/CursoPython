# Logical operators

'''
and (and) or (or) not (not)
and - all conditions need to be true
If any value is considered false, the entire expression will be evaluated as false.
 0 0.0 '' false 
# There is also the value None, which is used to represent the absence of a value or a null value.
'''

user_input = input('Do you want to enter the system? [y/n] ')
digit_password = input('Enter the password: ')
correct_password = '123'

if user_input == 'y' and digit_password == correct_password:
    print('Welcome to the system!')
elif user_input == 'y' and digit_password != correct_password:
    print('Incorrect password!')
else:
    print('System logged out!')
    
    
if (user_input == 'y' or user_input == 'Y') and digit_password == correct_password:
    print('Welcome to the system!')
elif user_input == 'y' and digit_password != correct_password:
    print('Incorrect password!')
else:
    print('System logged out!')