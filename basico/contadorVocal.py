
"""Contador de vocales

Solicita una palabra y cuenta cuántas vocales tiene."""

vocales = ["a","e","i","o","u"]
contador = 0
palabra = input("ingrese una palabra\n")

for char in list(palabra):
    if (char in vocales):
        contador += 1

print(f"la palabra {palabra} tiene {contador} vocales")