while True:
    try:
        num = int(input("Digite um número POSITIVO: "))
        num_lim = num
        if num > 0:
            num = num - (num * 2)
            while num <= num_lim:
                print(num)
                num = num + 1
            print("Fim.")
            break
        elif num < 0:
            print("ERRO: Você digitou um número negativo. Tente novamente.")
        else:
            print("ERRO: Você digitou o número zero, que não é positivo. Tente novamente.")
    except ValueError:
            print("ERRO: Por favor, digite um número válido (positivo).")