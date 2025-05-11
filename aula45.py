'''
generator - can pause the execution of a function and return a value
'''

# def generator(n=0, maximum=10):
#     while True:
#         yield n
        
#         n += 1
        
#         if n >= maximum:
#             return

        
# gen = generator()
# for n in gen:
#     print(n)


def gen1():
    yield 1
    yield 2
    yield 3
    
def gen2():
    yield from gen1()
    yield 4
    yield 5
    
g = gen2()
for number in g:
    print(number)