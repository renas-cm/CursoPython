# conditions
'''
if else --> if elif
'''
# BMI calculation
name = input('What is your name? ')
height = float(input('What is your height? '))
weight = float(input('What is your weight? '))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f'{name}, you are underweight!')
elif 18.5 <= bmi < 25:
    print(f'{name}, you are at a healthy weight!')
elif 25 <= bmi < 30:
    print(f'{name}, you are overweight!')
elif 30 <= bmi < 35:
    print(f'{name}, you have obesity grade 1!')
    
# input and output

in_out = input('do you want to login or logout')

if in_out == 'login':
    print('Welcome')
elif in_out == 'logout':
    print('Goodbye')
else:
    print('Invalid option')