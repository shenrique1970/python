lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = [
    # Para cada x tenho uma letra de sergio
    [(x, letra) for letra in 'Sergio']
    for x in range(3)
]

print(lista)
