cidadeA = 80000
cidadeB= 200000
ano = 0

while cidadeA <= cidadeB:
    cidadeA += cidadeA * 0.03
    cidadeB += cidadeB * 0.015
    ano += 1

print('População Cidade A:', cidadeA)
print('População Cidade B:', cidadeB)
print('Cidade A passa ou fica igual a Cidade B em número habitantes em %d anos' %ano)