n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
n5 = float(input("Digite o quinto número: "))

numeros = [n1, n2, n3, n4, n5]
soma = 0
tamanho = len(numeros)

for i in numeros:
    soma += i

media = soma / tamanho

print(f'A média aritmética dos cinco números é: {media}')