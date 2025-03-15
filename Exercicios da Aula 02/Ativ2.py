# 2- Escreva um programa em Python que solicite ao usuário o salário atual e mostre o 
# salário acrescido de 5% de comissão.

salario_atual = float(input("Digite o seu salário atual: "))
 
comissao = salario_atual * 0.05
novo_salario = salario_atual + comissao
 
print(f"O salário atual com 5% de comissão é: R$ {novo_salario:.2f}")