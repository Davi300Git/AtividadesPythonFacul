# 6- Escreva um programa em Python que leia um valor representando o gasto realizado por um
#  cliente do restaurante ComaBem e visualize o valor total a ser pago, considerando os 10% do garçom.

gasto = float(input("Digite o valor gasto no restaurante: R$ "))
 
taxa_garcom = gasto * 0.10
 
total_pagar = gasto + taxa_garcom
 
print(f"O valor total a ser pago, incluindo os 10% do garçom, é: R$ {total_pagar:.2f}")