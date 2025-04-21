'''
introduction try/except
try -> except 
try -> try to excute the code
except -> if an error occurs, execute this code
'''

name = input('whats your name?')

try:
    print(f'Hello {float(name)}')
except:
    print('Error: try to show your name')