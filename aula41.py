"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Sérgio Henrique'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):    # emquanto indice for menor que 14
    letra = nome[indice]    #letra igual nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)