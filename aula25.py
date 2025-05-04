'''
Write a program that asks the user to enter an integer number,
informs whether this number is even or odd. If the user does not enter an integer
number, inform that it is not an integer number.
'''

number = input('Type a integer number: ')

'''
for caract in number:
    if caract == '':
        del number[i]
    elif number.isdigit():
        if int(number) % 2 == 0:
            print(f'{number} are integer and is even')
        elif(int(number) % 2 != 0):
            print(f'{number} are integer and is odd')
        else:
            print(f'{number} is not an integer number')
    break
'''

if number.isdigit():
    if int(number) % 2 == 0:
        print(f'{number} is even and its integer')
    else:
        print(f'{number} is odd and its integer')
else:
    print(f'{number} is not an integer number')
    
    
'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

horario = int(input('Digite a hora: '))

if horario >= 0 and horario <= 11:
    print('Bom dia')
elif horario >= 12 and horario <= 17:
    print('Boa tarde')
elif horario >= 18 and horario <= 23:
    print('Boa noite')
    
'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')