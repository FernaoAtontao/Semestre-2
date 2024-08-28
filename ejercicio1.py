class Persona:
    def __init__(self, nombre, edad, altura=0.0, peso=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
    def calcular_imc(self):
        if self.altura <= 0:
            raise ValueError("La altura debe ser mayor que cero para calcular el IMC.")
        imc = self.peso / (self.altura ** 2)
        if imc < 18.5:
            estado = "bajo peso"
        elif 18.5 <= imc < 24.9:
            estado = "peso normal"
        elif 25 <= imc < 29.9:
            estado = "sobrepeso"
        else:
            estado = "obesidad"
        print(f"El IMC de {self.nombre} es {imc:.2f}, que se considera {estado}.")
        return imc
    def promedio_asignatura(self, nota1, nota2, nota3):
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 4.0:
            print(f"{self.nombre} aprobó la asignatura con un promedio de {promedio:.2f}.")
        else:
            print(f"{self.nombre} no aprobó la asignatura con un promedio de {promedio:.2f}.")
        return promedio
persona1 = Persona(nombre="Fernando", edad=19, altura=1.7, peso=123)
persona1.calcular_imc()
persona1.promedio_asignatura(5.5, 4.5, 5.0)