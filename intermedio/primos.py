"""Generador de números primos optimizado"""

def es_primo(numero):
    """Determina si un número es primo usando una verificación optimizada."""
    if numero < 2:
        return False
    if numero == 2:  # 2 es el único número primo par
        return True
    if numero % 2 == 0:  # Excluye otros pares
        return False

    for i in range(3, int(numero ** 0.5) + 1, 2):  # Solo verificamos impares hasta √n
        if numero % i == 0:
            return False
    return True

def primos(n):
    """Genera los primeros N números primos"""
    lista_primos = []
    numero = 2  # Comenzamos desde el primer número primo

    while len(lista_primos) < n:
        if es_primo(numero):
            lista_primos.append(numero)
        numero += 1  # Avanzamos al siguiente número

    return lista_primos

# Ejemplo de uso
print(primos(10))
