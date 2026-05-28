import time

def campeao(L,V):
    return(L.index(V)) + 1

anos_ganhos = []

print("Escolha o país que você quer checar:")
print("Brasil -> Digite BR")
print()
sel = input("Entrada: ")
print("")

if sel == "BR":
    anos_ganhos = [1958, 1962, 1970, 1994, 2002]

ano_de_copa = 1926
anos_com_copa = []

for i in range(1,23):
    ano_de_copa += 4
    anos_com_copa.append(ano_de_copa)

for i in range(0,5):
    anos_com_copa.remove(anos_ganhos[i])

while True:
    ano = int(input("Escolha um ano (Digite 0 para encerrar o programa): "))

    if ano == 0:
        break
    elif ano not in anos_ganhos and ano in anos_com_copa:
        print("O Brasil não ganhou a Copa do Mundo nesse ano. :( \n")
    elif ano >= 2026:
        print("As Copas do Mundo de 2026 em diante ainda não foram encerradas. :/\n")
    elif ano in anos_ganhos:
        print(f'{campeao(anos_ganhos, ano)}º vez campeão em {ano} :D \n')
    else:
        print("Não teve Copa do Mundo nesse ano. ;-;")
    time.sleep(5)
    print("tá achando o programa uma merda né")
    time.sleep(5)
    print("ent toma")
    time.sleep(3)
    while True:
        print("BANDIDO")
        time.sleep(0.5)
        print("QUER")
        time.sleep(0.5)
        print("67")
        time.sleep(0.5)
        print("RESENHA")
        time.sleep(0.5)
exit
