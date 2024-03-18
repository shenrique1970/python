"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[0])    # indice 0
print(variavel[4:8])    # do indice 4 ao 8
print(variavel[4:])    # do indice 4 ao final
print(variavel[0:9:2])   # de 0 a 9 de 2 em 2
print(variavel[::-1])    # de tras pra frente