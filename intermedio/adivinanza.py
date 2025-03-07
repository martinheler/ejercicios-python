"""Juego de adivinanza
Genera un número aleatorio y pide al usuario que lo adivine, dándole pistas de "más alto" o "más bajo".
"""

"""Juego de Adivinanza Mejorado"""

import random

# Genera un número aleatorio entre 1 y 20
num = random.randint(1, 20)
adivino = False  # Booleano que indica si se adivinó el número

print("🎯 Adivina el número (entre 1 y 20)")
print("🔹 Si el número ingresado es menor, aparecerá: 'El número a adivinar es mayor'")
print("🔹 Si el número ingresado es mayor, aparecerá: 'El número a adivinar es menor'")

while not adivino:
    try:
        numero = int(input("Ingrese un número: "))
        
        if numero < num:
            print("📈 El número a adivinar es mayor.")
        elif numero > num:
            print("📉 El número a adivinar es menor.")
        else:
            adivino = True
            print(f"🎉 ¡Felicidades! Adivinaste el número {num} 🎉")

    except ValueError:
        print("⚠️ Entrada inválida. Ingresa un número entero.")

