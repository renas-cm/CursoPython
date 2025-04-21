# type conversion, type coercion, typecasting
# immutable and primitive types: str, int, float, and bool

print(1 + 1)

# you cannot concatenate a str with an int
# print('1' + 1) --> TypeError: can only concatenate str (not "int") to str

# polymorphism --> concatenation
print('a' + 'b')

# converts the str '1' to the int 1
print(int('1') + 1) 

# converts the int 1 to the float 1.0
print(float('1') + 1)
print(float('1.2') + 1) 

# empty string = False 
print(bool(''))
# string with spaces = True
print(bool(' '))
