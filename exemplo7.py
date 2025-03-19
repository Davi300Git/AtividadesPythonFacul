import math

num = int(input("Digite um número: "))
if num > 0 :
    r = math.sqrt(num)
    print("A raiz quadrada de %.2f é %.2f:" % (num,r))
else:
    print("Não é possível calcular a raiz de número nagativo")