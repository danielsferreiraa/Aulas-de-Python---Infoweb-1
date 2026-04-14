cont = 1
acum = 0

while cont <= 10:
    if cont % 2 == 0:
        print(cont)
        acum = acum + cont
        cont = cont + 1
    else:
        cont = cont + 1
print(f'Total Acumulado: {acum}')
print("Fim.")