# in and not in operators
# in and not in operators are used to check if a value is present in a sequence (like a list, tuple, or string) or not.
# The not in operator is the opposite of the in operator.

# 0 1 2 3 4 5
# R e n a t o
# -5 -4 -3 -2 -1

name = input('type your name')
find = input('type a letter to find in your name')

print(name[0])  # R
print(name[-5])  # R

print('R' in name)  # True
print('h' in name)  # False

if find in name:
    print(f'letter {find} is in your name')
else:
    print(f'letter {find} is not in your name')