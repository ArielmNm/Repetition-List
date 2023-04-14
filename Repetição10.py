num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))


if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1


for i in range(menor, maior+1):
    print(i)