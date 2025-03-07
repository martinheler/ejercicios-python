
"""Ordenador de listas - Algoritmo de Burbuja optimizado"""

def bubble_sort(lista):
    """Ordena una lista usando el algoritmo de burbuja optimizado."""
    n = len(lista)
    for i in range(n):
        intercambiado = False  # Verifica si hubo cambios en esta pasada
        for j in range(n - 1 - i):  # Últimos elementos ya estarán ordenados
            if lista[j] > lista[j + 1]:  # Si están en el orden incorrecto, intercambiar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:  # Si no hubo intercambios, la lista ya está ordenada
            break
    return lista

def selection_sort(lista):
    """Ordena una lista usando el algoritmo de selección."""
    n = len(lista)
    for i in range(n):
        min_idx = i  # Suponemos que el elemento actual es el menor
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:  # Buscamos el mínimo en la parte no ordenada
                min_idx = j
        # Intercambiamos el mínimo encontrado con el primer elemento no ordenado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Ejemplo de uso
lista = [10, 3, 7, 1, 4, 6, 8, 2, 5]
print(selection_sort(lista))

