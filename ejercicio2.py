class Coche:
    def __init__(self, marca, gasolina=0.0):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = 0.0

    def conducir(self, kilometros):
        # Calcula cuántos litros de gasolina se necesitarán para recorrer la distancia
        litros_necesarios = kilometros / 10
        
        if litros_necesarios > self.gasolina:
            # Si no hay suficiente gasolina, conduce solo lo que alcance
            kilometros_recorridos = self.gasolina * 10
            self.kilometros_recorridos += kilometros_recorridos
            self.gasolina = 0
            print(f"Se ha quedado sin gasolina. Solo pudo recorrer {kilometros_recorridos} kilómetros.")
        else:
            # Si hay suficiente gasolina, recorre la distancia completa
            self.kilometros_recorridos += kilometros
            self.gasolina -= litros_necesarios
            print(f"Se han recorrido {kilometros} kilómetros. Gasolina restante: {self.gasolina:.2f} litros.")

    def cargar_gasolina(self, litros):
        self.gasolina += litros
        print(f"Se han añadido {litros} litros de gasolina. Gasolina total: {self.gasolina:.2f} litros.")

# Ejemplo de uso:
coche1 = Coche(marca="Toyota", gasolina=5.0)
coche1.conducir(30)  # Intentará conducir 30 kilómetros
coche1.cargar_gasolina(10)  # Agrega 10 litros de gasolina
coche1.conducir(50)  # Intentará conducir 50 kilómetros
