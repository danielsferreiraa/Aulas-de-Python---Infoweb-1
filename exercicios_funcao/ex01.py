def soma(a, b, c):
    return a + b + c
rep = 0

while rep != 2:
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    n3 = int(input("Digite o terceiro número inteiro: "))
    print(soma(n1, n2, n3))

    rep += 1