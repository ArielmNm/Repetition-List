numeros = []

for u in range(5):
    numero = float(input(f"Digite o {u+1}º número: "))
    numeros.append(numero)

maior_numero = max(numeros)

print(f"O maior número é {maior_numero}.")
