def prod(a, b):
    return a * b
rep = 0

while rep != 2:
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    print(prod(n1, n2))
    rep += 1