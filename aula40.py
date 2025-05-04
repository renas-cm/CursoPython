'''
set
'''

s1 = set('abracadabra') 
# random order {'a', 'b', 'c', 'd', 'r'}
print(s1)

s2 = set()
s2 = {'abracadabra'}
print(s2)

l1 = [1, 2, 3, 4, 4, 5]
ss1 = set(l1)
l2 = list(ss1)
print(l1)

print(4 in ss1)

for i in ss1:
    print(i)
    
# methods 

set = set()
set.add('number')
set.update(['number3'])
set.update('number')
set.update(('Hello World',1, 2, 3))
# set.clear()
set.discard('number')
print(set)


set2 = {1,2,3}
set3 = {2,3,4}
print(set2 | set3) 
print(set2 & set3)
print(set2 - set3)
print(set2 ^ set3)