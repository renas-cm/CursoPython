# Comentário explicativo: Este código demonstra o uso da função print com diferentes parâmetros.

# \r\n -> CRLF: Representa a quebra de linha no Windows.
# \n -> LF: Representa a quebra de linha no Linux/Mac.

# Exemplo 1: Imprime os números 12, 34 e 1011
# 'sep' define o separador entre os valores (aqui é uma string vazia "")
# 'end' define o que será adicionado ao final da linha (aqui é '#')
print(12, 34, 1011, sep="", end='#')

# Exemplo 2: Imprime os números 56 e 78
# 'sep' define o separador entre os valores (aqui é '-')
# 'end' define o que será adicionado ao final da linha (aqui é '\n', que quebra a linha)
print(56, 78, sep='-', end='\n')

# Exemplo 3: Imprime os números 9 e 10
# 'sep' define o separador entre os valores (aqui é '-')
# 'end' define o que será adicionado ao final da linha (aqui é '\n', que quebra a linha)
print(9, 10, sep='-', end='\n')

# Erro no código original:
# A palavra 'Print' com a inicial maiúscula não é reconhecida como uma função válida em Python.
# A função correta é 'print' (tudo em letras minúsculas).
# Corrigido removendo ou ajustando a linha.