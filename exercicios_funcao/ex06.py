def soma_ate_n(n):
    soma = 0
    if n > 0:
        for i in range(1, n+1):
            soma += i
        return soma
    else:
        return "ERRO"

rep = 0

while rep != 2:
    num = int(input("Digite um número inteiro: "))
    print(soma_ate_n(num))
    rep += 1