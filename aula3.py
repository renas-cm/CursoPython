"""
Python = Programming Language
# Explains that Python is a language used to write programs (code that the computer understands).

Typing type = Dynamic / Strong
# Dynamic typing: you don't need to declare the variable type (e.g., int, str, etc.).
# Strong typing: Python does not automatically convert types in incompatible operations (e.g., it doesn't add a string to a number without conversion).

str -> string -> text
# Shows that the type 'str' means string, which is nothing more than text.

Strings are texts enclosed in quotes
# Explains that to create a string (text) in Python, we use single or double quotes.
"""

# Single quotes
print('Text with single quotes')

# Double quotes
print("Text with double quotes")

# Escape
print("Text \"Escape\"")

# r
print(r"Text \"with raw\"") 

# f
name = "Tulip"
print(f"Hello, {name}!")

"""
The f in Python is used to create f-strings, which are formatted strings. This means you can insert variables or expressions directly into the text in a practical and elegant way.

* The f before the string indicates that it is formatted.
* What is inside {} will be evaluated as Python code.
* In the example above, {name} will be replaced by "Tulip".
"""