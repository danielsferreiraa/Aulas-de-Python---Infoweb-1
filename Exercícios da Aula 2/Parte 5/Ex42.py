Prod = input("Insira o nome do produto: ")
Preco = float(input("Insira o preço desse produto: "))
Quant = int(input("Insira a quantidade de unidades a serem compradas desse produto: "))

Total = Preco * Quant

print(Quant,"unidades de",Prod,"custarão: R$",Total)