#4 Escreva um programa em Python que calcule as duas raízes de uma equação de 2º grau ax²+bx+c,
#  conhecendo os valores dos coeficientes da mesma (a, b, c). Suponha que as raízes são reais. 
# Lembre-se que para calcular as duas raízes: 

import math

a = float(input("Digite o valor de a (diferente de zero): "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
 
delta = b**2 - 4*a*c
 
if delta >= 0:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
 
    print(f"As raízes da equação são: {raiz1:.2f} e {raiz2:.2f}")
else:
    print("A equação não possui raízes reais.")