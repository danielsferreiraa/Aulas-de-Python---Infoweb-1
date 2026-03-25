val = float(input("Insira o valor do produto: "))
desc = float(input("Insira o percentual de desconto: "))

valf = val - (val * desc / 100)

print("O valor final após o desconto é: R$", valf)