"""
Python = Linguagem de programação
# Explica que Python é uma linguagem usada para escrever programas (códigos que o computador entende).

Tipo de tipagem = Dinâmica / Forte
# Tipagem dinâmica: você não precisa declarar o tipo da variável (ex: int, str etc.).
# Tipagem forte: o Python não converte tipos automaticamente em operações incompatíveis (ex: não soma string com número sem conversão).

str -> string -> texto
# Mostra que o tipo 'str' significa string, que nada mais é do que um texto.

Strings são textos que estão dentro de aspas
# Explica que para criar uma string (texto) em Python, usamos aspas simples ou duplas.
"""

# Aspas simples
print('Texto com aspas simples')

# Aspas Duplas
print("Texto com aspas duplas")

#Escape
print("Texto \"Escape\"")

#r
print(r"Texto \"com raw\"") 

#f
"""
O f no Python é usado para criar f-strings, que são strings formatadas. Isso significa que você pode inserir variáveis ou expressões diretamente dentro do texto de forma prática e elegante.

* O f antes da string indica que ela é formatada.
* O que estiver entre {} será avaliado como código Python.
* No exemplo acima, {nome} será substituído por "Tulipa".
"""
nome = "Tulipa"
print(f"Olá, {nome}!")