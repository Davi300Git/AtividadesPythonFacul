#7- Escreva um programa em Python que obtenha uma temperatura em graus Celsius, 
# calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin.

celsius = float(input("Digite a temperatura em graus Celsius: "))
 
fahrenheit = (9/5) * celsius + 32
 
kelvin = celsius + 273.15
 
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")
print(f"A temperatura em Kelvin é: {kelvin:.2f} K")