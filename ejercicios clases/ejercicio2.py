class Auto:
    def __init__(self, marca, gasolina=0.0):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = 0.0
    def manejar(self, kilometros):
        litros_necesarios = kilometros / 10
        if litros_necesarios > self.gasolina:
            kilometros_recorridos = self.gasolina * 10
            self.kilometros_recorridos += kilometros_recorridos
            self.gasolina = 0
            print(f"Se te quedó sin gasolina. Solo pudiste recorrer {kilometros_recorridos} kilómetros.")
        else:
            self.kilometros_recorridos += kilometros
            self.gasolina -= litros_necesarios
            print(f"Recorriste {kilometros} kilómetros. Gasolina restante: {self.gasolina:.2f} litros.")
    def cargar_gasolina(self, litros):
        self.gasolina += litros
        print(f"Agregaste {litros} litros de gasolina. Gasolina total: {self.gasolina:.2f} litros.")
auto1 = Auto("Toyota", 5.0)
auto1.manejar(30)
auto1.cargar_gasolina(10)
auto1.manejar(50)