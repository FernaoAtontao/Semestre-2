class Persona:
    def __init__(self, nombre, edad, altura=0.0, peso=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
        if self.altura <= 0:
            raise ValueError("La altura tiene que ser más grande que cero.")
        imc = self.peso / self.altura ** 2
        estado = ("bajo peso" if imc < 18.5 else
                  "peso normal" if imc < 25 else
                  "sobrepeso" if imc < 30 else
                  "obesidad")
        print(f"El IMC de {self.nombre} es {imc:.2f}, que se considera {estado}.")
        return imc

    def promedio_asignatura(self, *notas):
        promedio = sum(notas) / len(notas)
        resultado = "aprobó" if promedio >= 4.0 else "no aprobó"
        print(f"{self.nombre} {resultado} la asignatura con un promedio de {promedio:.2f}.")
        return promedio

persona1 = Persona("Fernando", 19, 1.7, 123)
persona1.calcular_imc()
persona1.promedio_asignatura(5.5, 4.5, 5.0)