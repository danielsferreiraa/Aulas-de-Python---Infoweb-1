while True:
    num = int(input("Digite um número inteiro positivo: "))

    cont = 1
    acum = 0

    if num > 0:
        while cont <= num:
            if cont % 3 == 0:
                acum = acum + cont
                cont = cont + 1
            else:
                cont = cont + 1
        print(f'A soma dos múltiplos de 3 compreendidos entre 1 e {num} é: {acum}')
        print("Fim.")
    else:
        print("ERRO: Por favor, digite um número inteiro positivo.")