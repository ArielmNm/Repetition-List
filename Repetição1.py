print("insira um valor de 0-10:")
nota = int(input())

while nota >= 10 or nota <= 0:
    print("valor invalido!!!-insira um valor de 0-10:")
    nota = int(input())
print("valor valido!")