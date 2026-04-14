while True:
    num = int(input("Digite um número inteiro positivo: "))

    cont = 1
    prod = 1

    if num > 0:
        while cont <= num:
            prod = prod * cont
            cont = cont + 1
        print(f'O produtório dos números inteiros de 1 a {num} é: {prod}')
        print("Fim.")
    else:
        print("ERRO: Por favor, digite um número inteiro positivo.")