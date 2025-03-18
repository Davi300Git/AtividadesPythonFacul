# Faça uma programa em Python que peça do usuário um valor em graus para um ângulo.
#  Converta-o para radianos e, usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo.

import math

# Solicita ao usuário o valor do ângulo em graus
angulo_graus = float(input("Digite o valor do ângulo em graus: "))

# Converte o ângulo de graus para radianos
angulo_radianos = math.radians(angulo_graus)

# Calcula o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Exibe os resultados
print(f"Ângulo em radianos: {angulo_radianos:.4f}")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")