idade = [10, 11, 11, 12, 16]
altura = [1.50, 1.55, 1.58, 1.60, 1.80]
idadevazia = []
alturavazia = []

print("idades:", idade)
print("altura", altura)

for i in range(5):
    idadevazia.append(idade.pop())
    alturavazia.append(altura.pop())

print(idadevazia)
print(alturavazia)