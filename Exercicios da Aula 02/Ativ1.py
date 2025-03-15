# 1- Desenvolva um programa em Python que solicite ao usuário os valores dos lados de um retângulo
#  e calcule e mostre seu perímetro e sua área.

lado1 = float(input("Digite o valor do primeiro lado do retângulo: "))
lado2 = float(input("Digite o valor do segundo lado do retângulo: "))
 
perimetro = 2 * (lado1 + lado2)
 
area = lado1 * lado2
 
print(f"O perímetro do retângulo é: {perimetro}")
print(f"A área do retângulo é: {area}")