while True:
    num = int(input("Digite um número positivo: "))
    tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    produto = 0

    if num > 0:
        for i in tabuada:
            produto = num * i
            print(f'{num} x {i} = {produto}')
        break
    else:
        print("ERRO. Tente novamente com um número positivo.")