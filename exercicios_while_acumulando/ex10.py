while True:
    contador = int(input("Digite um número entre 1 a 10: "))
    intervalo_correto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    coletor_de_num = 1
    num = 0
    resultado_da_soma = 0

    if contador in intervalo_correto:
        while coletor_de_num <= contador:
            num = int(input(f'Número {coletor_de_num}: '))
            resultado_da_soma = resultado_da_soma + num
            coletor_de_num = coletor_de_num + 1
        print(f'Resultado da Soma = {resultado_da_soma}')
        print("Fim.")
    else:
        print("Valor Inválido")
        
        

