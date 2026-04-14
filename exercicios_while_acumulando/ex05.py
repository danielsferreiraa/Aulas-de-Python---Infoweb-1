cont = 1
prod = 1

while cont <= 8:
    if cont % 2 != 0:
        print(cont)
        prod = prod * cont
        cont = cont + 1
    else:
        cont = cont + 1
print(f'Produtório: {prod}')
print("Fim.")
