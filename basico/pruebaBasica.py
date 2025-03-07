import unicodedata

class Basico:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def suma(self):
        return self.x + self.y
    
    def pruebapar(self, numero):
        return f"El número {numero} es {'par' if numero % 2 == 0 else 'impar'}"
    
    def conversor(self, temp, tipo):
        if tipo.lower() == 'c':  # Celsius a Fahrenheit
            return f"{temp}°C son {(temp * 9/5) + 32}°F"
        elif tipo.lower() == 'f':  # Fahrenheit a Celsius
            return f"{temp}°F son {(temp - 32) * 5/9}°C"
        else:
            return "Opción no válida"

    def areatriangulo(self):
        return (self.x * self.y) / 2
    
    def contadorvocal(self, palabra):
        vocales = "aeiouáéíóú"
        palabra = unicodedata.normalize('NFD', palabra).encode('ascii', 'ignore').decode('utf-8')  # Normaliza para quitar tildes
        return sum(1 for char in palabra.lower() if char in vocales)

    def interactuar(self):
        """Función para interactuar con el usuario y probar los métodos."""
        print("\nElige una opción:")
        print("1. Suma de dos números")
        print("2. Verificar si un número es par o impar")
        print("3. Conversor de temperatura")
        print("4. Área de un triángulo")
        print("5. Contar vocales en una palabra")
        
        try:
            opcion = int(input("Ingrese el número de la opción deseada: "))
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            return

        match opcion:
            case 1:
                x = float(input("Ingrese el primer número: "))
                y = float(input("Ingrese el segundo número: "))
                self.x, self.y = x, y
                print("Resultado:", self.suma())

            case 2:
                num = int(input("Ingrese un número: "))
                print(self.pruebapar(num))

            case 3:
                temp = float(input("Ingrese la temperatura: "))
                tipo = input("Ingrese 'C' si está en Celsius o 'F' si está en Fahrenheit: ")
                print(self.conversor(temp, tipo))
            
            case 4:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                self.x, self.y = base, altura
                print("El área del triángulo es:", self.areatriangulo())

            case 5:
                palabra = input("Ingrese una palabra: ")
                print(f"La palabra '{palabra}' tiene {self.contadorvocal(palabra)} vocales.")
            
            case _:
                print("Opción no válida.")
     


# Ejemplo de uso interactivo
if __name__ == "__main__":
    basico = Basico()

    while True:
        basico.interactuar()
        repetir = input("¿Desea repetir? ('s' para sí, 'n' para no): ").strip().lower()
        if repetir == 'n':
            print("Saliendo del programa. ¡Hasta la próxima!")
            break
