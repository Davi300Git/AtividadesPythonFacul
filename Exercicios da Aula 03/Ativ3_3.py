#  Escreva um programa em Python para calcular o valor de uma prestação em atraso (prestacao).
#  Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de multa pelo atraso (multa) e 
# a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o valor da prestação atualizado, sabendo que: 
# prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

valorPrestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite a porcentagem de multa pelo atraso (%): "))
qtdeDias = int(input("Digite a quantidade de dias de atraso: "))

# Calcula o valor da prestação atualizado
prestacao = valorPrestacao + (valorPrestacao * (multa / 100) * qtdeDias)

# Exibe o valor da prestação atualizado
print(f"O valor da prestação atualizado é: R$ {prestacao}")