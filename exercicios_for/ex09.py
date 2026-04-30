n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))

numeros = [n1, n2, n3, n4, n5]
soma = 0

for i in numeros:
    soma += i
print(f'A soma total dos cinco números é: {soma}')
