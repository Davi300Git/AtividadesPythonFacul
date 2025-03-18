# Crie um programa em Python que solicite ao usuário a sua idade expressa em anos,
#  meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas em dias.
# Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.

anos = float(input("Informe a sua quantidades de anos : "))
meses = float(input("Informe a sua quantidades de meses : "))
dias = float(input("Informe a sua quantidades de dias : "))

totalDias = (anos * 365) + (meses * 30) + dias

print(f"Sua idade expressa em dias é: {totalDias} dias.")