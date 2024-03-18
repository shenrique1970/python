"""
Valores padão para parametros
aodefinir uma função, os parametros podem
ter valores padrão. Caso o valor não seja 
eniviado para o parametro, o valor padrão será usado.
Refatorar: Editar o seu código.
"""


def soma(x, y, z):
    if z is not None:
        print(f'{x=} y={y} {z=}', x + y + z)
    else:
        print(f'{x=} y={y} ', x + y)


soma(1, 2, 3)
soma(1, 2, 5)

soma(1, 2, 3,)
