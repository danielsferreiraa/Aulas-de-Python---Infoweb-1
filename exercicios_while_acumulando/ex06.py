while True:

    num = int(input("Digite um número inteiro positivo: "))
    cont = 1
    acum = 0

    if num > 0:
        while cont <= num:
            acum = acum + cont
            cont = cont + 1
        print(f'Soma dos números inteiros de 1 a {num} é: {acum}')
        print("Fim.")
    else:
        print("ERRO: Por favor, digite um número positivo.")