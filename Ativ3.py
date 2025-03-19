a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a < b and a < c:
    print(f"O primeiro número({a}) é o menor")
elif b < a and b < c:
    print(f"O segundo número({b}) é o menor")
else :
    print(f"O terceiro número({c}) é o menor")