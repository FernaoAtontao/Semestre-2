class Persona:
    nombre = "Cristina"
    apellido = "Torres"
    edad = 23
    def hablar(self):
        print (f"{self.nombre} está hablando")
    def caminar(self):
        print (f"{self.nombre} está caminando")

persona1 = Persona()
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")
persona1.hablar()
persona1.caminar()