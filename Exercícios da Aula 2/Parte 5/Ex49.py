horas = float(input("Insira a quantidade de horas trabalhadas: "))
valor = float(input("Insira o valor pago por hora trabalhada: "))

salt = horas * valor

print(f'O salário total do trabalhador é de: R${salt:.2f}')