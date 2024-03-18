import importlib

import aula117_m

print(aula117_m.variavel_modulo)

for i in range(10):
    importlib.reload(aula117_m)
    print(i)

print('Fim')
