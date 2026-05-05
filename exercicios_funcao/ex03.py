def par_ou_impar(a):
    if a % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

rep = 0

while rep != 2:
    num = int(input("Digite o número inteiro para checar se é par ou ímpar: "))
    print(par_ou_impar(num))
    rep += 1