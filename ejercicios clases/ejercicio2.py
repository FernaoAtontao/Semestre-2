class Coche:
    def __init__(self, marca, gasolina=0.0):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = 0.0
    def conducir(self, kilometros):
        litros_necesarios = kilometros / 10
        if litros_necesarios > self.gasolina:
            kilometros_recorridos = self.gasolina * 10
            self.kilometros_recorridos += kilometros_recorridos
            self.gasolina = 0
            print(f"Se ha quedado sin gasolina. Solo pudo recorrer {kilometros_recorridos} kilómetros.")
        else:
            self.kilometros_recorridos += kilometros
            self.gasolina -= litros_necesarios
            print(f"Se han recorrido {kilometros} kilómetros. Gasolina restante: {self.gasolina:.2f} litros.")
    def cargar_gasolina(self, litros):
        self.gasolina += litros
        print(f"Se han añadido {litros} litros de gasolina. Gasolina total: {self.gasolina:.2f} litros.")
coche1 = Coche("Toyota", 5.0)
coche1.conducir(30)
coche1.cargar_gasolina(10)
coche1.conducir(50)