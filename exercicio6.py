# 1: Em Aplicativo - Guarde o nome e o consumo de bateria no próprio objeto aplicativo;

# 2: Em Celular - Verifique se o celular está ligado (self.ligado) E se a bateria é maior 
# ou igual ao consumo do objeto 'app' passado por parâmetro;

# 3: Em executar_app - Subtraia o consumo do aplicativo da bateria atual do celular,
# não deve ser possivel executar um app com o celular desligado,
# deve se mostrado na tela o nome do aplicativo que foi usado.

# 4: Crie dois objetos Aplicativo com consumos de bateria diferentes;
# 5: Crie um objeto Celular, ligue o aparelho e execute cada um dos aplicativos criados.
import time


class Aplicativo:
    def __init__(self, nome = str, consumo_bateria = int):
        self.nome = nome
        self.consumo_bateria = consumo_bateria


class Celular:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} foi ligado.")
        self.executar_app(app1= Aplicativo("Pou", 2),app2= Aplicativo("X", 5))

    def executar_app(self, app1, app2):
        if self.ligado == False:
            print("Não dá pra executar um app com o celular desligado.")
        resposta = int(input("Qual app você deseja executar?\n1)Pou\n2)X\n"))
        match resposta:
            case 1:
                print("Pou iniciado.")
                while True:
                    if self.bateria > 0:
                        self.bateria -= app1.consumo_bateria
                        print(f"Aplicativo {app1.nome} executado. Bateria restante: {self.bateria}%\n aperte 1 para continuar executando o app ou 0 para sair.")
                        resposta = int(input())
                        if resposta == 0:
                            print("Aplicativo finalizado.")
                            break
                        time.sleep(0.5)
                    else:
                        print("Bateria insuficiente para executar o aplicativo.")
                        break
            case 2: 
                print("X iniciado.")
                while True:
                    if self.bateria > 0:
                        self.bateria -= app2.consumo_bateria
                        print(f"Aplicativo {app2.nome} executado. Bateria restante: {self.bateria}%\n aperte 1 para continuar executando o app ou 0 para sair.")
                        resposta = int(input())
                        if resposta == 0:
                            print("Aplicativo finalizado.")
                            break
                        time.sleep(0.5)
                    else:
                        print("Bateria insuficiente para executar o aplicativo.")
                        break

def main():
    xiaomi = Celular("Xiaomi", "Redmi Note 11S",100)
    if xiaomi.ligado == False:
        resposta = input("Deseja ligar o celular?(sim/nao) \n").strip().lower()
        match resposta:
            case "sim":
                if xiaomi.bateria > 0 and xiaomi.bateria <= 100:
                    xiaomi.ligar()
                    
                else:
                    print("sem bateria para ligar.")
            case _:
                if resposta != "sim":
                    print("Acabou")


if __name__ == "__main__":
    main()