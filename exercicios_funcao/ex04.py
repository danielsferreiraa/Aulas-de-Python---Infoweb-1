def menor_e_maior(a, b, c, d, e):
    lista = [a, b, c, d, e]
    return min(lista), max(lista)
rep = 0

while rep != 2:
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite um número inteiro: "))
    n3 = int(input("Digite um número inteiro: "))
    n4 = int(input("Digite um número inteiro: "))
    n5 = int(input("Digite um número inteiro: "))
    print(menor_e_maior(n1, n2, n3, n4, n5))
    rep += 1
