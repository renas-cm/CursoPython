questions = [
    {
        'question' : '2 + 2',
        'options' : ['1', '2', '3', '4'],
        'answer' : '4'
    },
    {
        'question' : '3 * 5',
        'options' : ['15', '10', '5', '20'],
        'answer' : '15'
    },
    {
        'question' : '10/2',
        'options' : ['5', '2', '10', '20'],
        'answer' : '5'
    },
]
for question in questions:
    print('Quanto é',question['question'])
    
    if question['options']:
        for i, option in enumerate(question['options']):
            print(f'{i})',option)
            
        answer = input('Escolha uma opção: ')
        if answer == question['answer']:
            print('Você acertou!')
        else:
            print('Você errou! \n')