class carro:
    def acelerar(self):
        return "O carro está acelerando"

class carroEsportivo(carro):
   pass

ferrari = carroEsportivo()
print(ferrari.acelerar()) #Saida: O carro está acelerando
