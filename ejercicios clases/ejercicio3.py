# EJERCICIOS DE CLASES
# Implementar una clase Fraccion que represente una fracción matemática con numerador y
# denominador. Además se debe crear varios métodos mágicos que permitan operar, comparar, y mostrar
# las fracciones de manera intuitiva. La clase debe poseer los siguientes métodos mágicos:
# Método mágico que devuelva la fracción como una representación de cadena
# Método mágico que permita sumar dos fracciones
# Método mágico que permita el producto entre dos fracciones
# Método mágico que permita comparar dos fracciones. Dos fracciones se consideran iguales si sus
# valores numéricos son equivalentes.

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, other):
        nuevo_numerador = self.numerador * other.denominador + other.numerador * self.denominador
        nuevo_denominador = self.denominador * other.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __mul__(self, other):
        nuevo_numerador = self.numerador * other.numerador
        nuevo_denominador = self.denominador * other.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __eq__(self, other):
        return self.numerador * other.denominador == other.numerador * self.denominador

# Ejemplo de uso
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(2, 4)

print(fraccion1)  # Output: 1/2
print(fraccion1 + fraccion2)  # Output: 1
print(fraccion1 * fraccion2)  # Output: 1/4
print(fraccion1 == fraccion2)  # Output: True