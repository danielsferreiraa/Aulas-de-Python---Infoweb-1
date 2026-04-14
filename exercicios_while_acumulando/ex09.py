while True:
    num = int(input("Digite um número que seja maior ou igual a zero: "))

    cont = 0
    acum = 0    
    if num >= 0:
        while cont <= num:
            acum = acum + 2 ** cont
            cont = cont + 1
        print(f'O resultado da soma acumulativa é: {acum}')
        print("Fim.")
    else: 
        print("ERRO: Por favor, digite um número que não seja negativo.") 