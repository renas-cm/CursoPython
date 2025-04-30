

word = 'girafa'
word_reveal = '******'

want_play = input('Do you want to play?')

while word = False
    trying = input('type the letter:')
    
    for i in word:
        if len(trying) = 1:
            if trying == i:
                print('letter found!')
                word_reveal = word_reveal.replace('*', i)
                print(word_reveal)
                if word_reveal == word:
                    print('you win!')
                    word_reveal = True
                    break
        
        else:
            print('invalid letter')
            
