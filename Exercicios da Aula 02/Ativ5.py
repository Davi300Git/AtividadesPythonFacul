# 5- Escreva um programa em Python que leia a cotação do dólar (taxa de conversão),
#  leia um valor em dólares e converta e mostre o valor equivalente em Reais. 

cotacao_dolar = float(input("Digite a cotação do dólar (em Reais): "))
valor_dolares = float(input("Digite o valor em dólares: "))
 
valor_reais = valor_dolares * cotacao_dolar
 
print(f"O valor equivalente em Reais é: R$ {valor_reais:.2f}")