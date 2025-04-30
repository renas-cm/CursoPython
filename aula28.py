'''
calculator
'''
want_calc = input('Do you want to calculate?')
operators = {'+': lambda x, y: x + y, 
             '-': lambda x, y: x - y, 
             '*': lambda x, y: x * y, 
             '/': lambda x, y: x / y if y != 0 else 'undefined'}

while want_calc == "yes":
    number = int(input('type the first number: '))
    operator = input('type the operator: ')
    number2 = int(input('type the second number: '))
    
    if operator in operators:
        result = operators[operator](number, number2)
        print(f'{number} {operator} {number2} = {result}')
    else:
        print('Invalid operator')
    
    want_calc = input('Do you want to calculate?')

print('GoodBye')