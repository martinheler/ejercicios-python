"""Cifrado César Mejorado"""

abecedario = "abcdefghijklmnñopqrstuvwxyz"  # Convertido a string para evitar indexaciones largas

def cifrar(palabra, semilla):
    """Cifra una palabra usando el Cifrado César"""
    palabra = palabra.lower()  # Convertir a minúsculas para evitar errores
    cifrado = ""

    for letra in palabra:
        if letra in abecedario:  # Solo cifrar si es una letra
            indice = abecedario.index(letra)
            salto = (indice + semilla) % len(abecedario)  # Evita desbordamientos
            cifrado += abecedario[salto]
        else:
            cifrado += letra  # Mantiene espacios y signos sin cambios

    return cifrado

def descifrar(palabra, semilla):
    """Descifra un mensaje usando el Cifrado César"""
    palabra = palabra.lower()
    descifrado = ""

    for letra in palabra:
        if letra in abecedario:
            indice = abecedario.index(letra)
            salto = (indice - semilla) % len(abecedario)  # Evita valores negativos
            descifrado += abecedario[salto]
        else:
            descifrado += letra  # Mantiene espacios y signos

    return descifrado

# Interacción con el usuario
print("🔐 Cifrado César")
palabra = input("Ingrese una palabra o frase: ")
semilla = int(input("Ingrese la semilla (número de desplazamiento): "))

texto_cifrado = cifrar(palabra, semilla)
print(f"🔒 Texto Cifrado: {texto_cifrado}")
print(f"🔓 Texto Descifrado: {descifrar(texto_cifrado, semilla)}")

