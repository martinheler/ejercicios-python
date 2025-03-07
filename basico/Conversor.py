"""Conversor de temperatura

Convierte una temperatura dada en Celsius a Fahrenheit y viceversa."""

temp = float(input("Ingrese la temperatura\n"))

print("¿la temperatura esta en Celsius?\n")
print("ingrese 's' para si, 'n' para no\n")

flag = input()

if (flag.lower()=='s'):
    Ftemp = (temp*(9/5))+32
    print(f"{temp} son {Ftemp}° farenheit")
elif(flag.lower()=='n'):
    Ftemp = ((temp-32)/1.8)
    print(f"{temp} son {Ftemp}° celsius")
else:
    print("opcion no valida")

