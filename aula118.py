import importlib

import aula118_m

print(aula118_m.variavel)

for i in range(10):
    importlib.reload(aula118_m)
    print(i)

print('Fim')
