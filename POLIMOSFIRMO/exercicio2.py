import os; os.system('clear')

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = 100  

    def acelerar(self):
        if self.combustivel > 0:
            self.combustivel -= 10
            print(f"O carro acelerou! Combustível restante: {self.combustivel}%")
        else:
            print("Sem combustível para acelerar!")

    def painel(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Combustível: {self.combustivel}%")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.bateria = 100 
        self.combustivel = None 

    def acelerar(self):
        if self.bateria >= 5:
            self.bateria -= 5
            print(f"O carro elétrico acelerou silenciosamente! Bateria restante: {self.bateria}%")
        else:
            print("Bateria insuficiente para acelerar!")

    def recarregar(self):
        self.bateria = 100
        print("Bateria recarregada para 100%!")

    def painel(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Bateria: {self.bateria}%")

carro1 = Carro("Chevrolet", "Opala")
carro1.painel()
carro1.acelerar()

print("-----")

carro2 = CarroEletrico("Tesla", "Model 3")
carro2.painel()
carro2.acelerar()
carro2.acelerar()
carro2.painel()
carro2.recarregar()
carro2.painel()
        