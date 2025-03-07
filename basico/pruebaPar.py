"""Par o impar

Pide un número al usuario e imprime si es par o impar."""

numero = float(input("Ingrese un numero\n"))

if (numero % 2 == 0):
    print(f"el numero {numero} es par")
else:
    print(f"el numero {numero} es impar")