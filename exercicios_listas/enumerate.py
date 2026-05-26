def mostrar_lista(L):
    for indice, valor in enumerate(L):
        print (f'{indice+1}:{valor}')

print(mostrar_lista([10, 20, 30]))