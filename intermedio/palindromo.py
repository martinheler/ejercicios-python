"""9.	Palíndromo
o	Crea una función que determine si una palabra o frase es un palíndromo.
"""

import unicodedata

def normalizar(texto):
    """Convierte texto a minúsculas, elimina espacios y tildes."""
    texto = texto.lower().replace(" ", "")  # Convierte a minúsculas y quita espacios
    texto = unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8")  # Elimina tildes
    return texto

def es_palindromo(palabra):
    """Verifica si una palabra o frase es un palíndromo."""
    palabra_limpia = normalizar(palabra)
    if palabra_limpia == palabra_limpia[::-1]:  # Invierte la cadena con slicing
        return f"✅ La palabra/frase '{palabra}' es un palíndromo."
    else:
        return f"❌ La palabra/frase '{palabra}' NO es un palíndromo."


# Prueba con entrada del usuario
"""
print("🔍 Comprobador de Palíndromos")
palabra = input("Ingrese una palabra o frase:\n")
print(es_palindromo(palabra))
"""
