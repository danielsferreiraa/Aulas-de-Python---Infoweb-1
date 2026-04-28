num = int(input("Digite um número inteiro positivo: "))
fator = 1

for i in range(num, 1, -1): # [1, num[
    fator *= i
print(fator)
# 10
# fat = 10 * (10 - 1) * (10 - 2) * (10 - 3) ... * (10 - 9)
# fat = (1 + 0) * (1 + 1) ... (1 + (10 -1))