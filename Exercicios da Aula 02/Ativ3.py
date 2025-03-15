# 3- Escreva um programa em Python que solicite ao usuário a distância entre duas 
# cidades e o tempo de viagem. O programa deverá calcular e exibir a velocidade média 
# de um carro que vai de uma cidade para outra. Utilize a fórmula:  vide Apresentação

distancia = float(input("Digite a distância entre as cidades (em km): "))
 
tempo = float(input("Digite o tempo de viagem (em horas): "))
 
velocidade_media = distancia / tempo
 
print(f"A velocidade média do carro é: {velocidade_media:.2f} km/h")