class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra):
        nuevo_numerador = self.numerador * otra.denominador + otra.numerador * self.denominador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __mul__(self, otra):
        nuevo_numerador = self.numerador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __eq__(self, otra):
        return self.numerador * otra.denominador == otra.numerador * self.denominador

fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(2, 4)

print(fraccion1)  # Output: 1/2
print(fraccion1 + fraccion2)  # Output: 1
print(fraccion1 * fraccion2)  # Output: 1/4
print(fraccion1 == fraccion2)  # Output: True