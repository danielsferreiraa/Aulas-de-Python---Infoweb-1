while True:
    try:
        num = int(input("Digite um número positivo: "))
        ultimo_num = num
        if num > 0:
            num = (num - num) + 1
            while num <= ultimo_num:
                print(num)
                num = num + 1
            print("Fim")
            break
        elif num < 0:
            print("ERRO: Você digitou um número negativo. Por favor, digite um positivo.")
        else:
            print("ERRO: Você digitou o número zero, que não é um número positivo. Tente novamente.")
    except ValueError:
        print("ERRO: Por favor, digite um número válido (Positivo).")