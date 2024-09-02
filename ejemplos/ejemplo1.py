class Persona():
    nombre = "Cristina"
    apellido = "Torres"
    edad = 23
    def hablaar(self):
        print (f"{self.nombre} esta hablando")
    def caminar(self):
        print (f"{self.nombre} esta caminando")

persona1 = Persona()
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")
persona1.hablaar()
persona1.caminar()