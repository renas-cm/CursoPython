word = 'python'
word_reveal = '*' * len(word)

want_play = input('Do you want to play? ')

if want_play.lower() == 'yes':
    while word_reveal != word:
        trying = input('Type the letter: ')
        
        if len(trying) == 1:
            if trying in word:
                print('Letter found!')
                word_reveal = ''.join(
                    trying if word[i] == trying else word_reveal[i]
                    for i in range(len(word))
                )
                print(word_reveal)
            else:
                print('Letter not found.')
            
            if word_reveal == word:
                print('You win!')
                break
        else:
            print('Invalid input. Please type a single letter.')
