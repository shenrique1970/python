a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'   # :.2f 1.10 duas casas decimais
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)