# 1: Em Aplicativo - Guarde o nome e o consumo de bateria no próprio objeto aplicativo;

# 2: Em Celular - Verifique se o celular está ligado (self.ligado) E se a bateria é maior 
# ou igual ao consumo do objeto 'app' passado por parâmetro;

# 3: Em executar_app - Subtraia o consumo do aplicativo da bateria atual do celular,
# não deve ser possivel executar um app com o celular desligado,
# deve se mostrado na tela o nome do aplicativo que foi usado.

# 4: Crie dois objetos Aplicativo com consumos de bateria diferentes;
# 5: Crie um objeto Celular, ligue o aparelho e execute cada um dos aplicativos criados.

class Aplicativo:
    def __init__(self, nome, consumo_bateria):
        self.nome = nome
        self.consumo_bateria = consumo_bateria


class Celular:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = True

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.marca} {self.modelo} foi ligado.")
        

    def executar_app(self, app):
        if self.ligado and self.bateria >= app.consumo_bateria:
            self.bateria -= app.consumo_bateria
            print(f"Executando o aplicativo: {app.nome}.")
            print(f"Bateria restante: {self.bateria}%.")

        else:
            if not self.ligado:
                print("O celular está desligado. Não é possível executar os aplicativos.")
            else:
                print(f"Bateria insuficiente para executar o aplicativo: {app.nome}.")
                print(f"Bateria atual: {self.bateria}%, consumo necessário: {app.consumo_bateria}%.")

    app1 = Aplicativo("WhatsApp", 10)
    app2 = Aplicativo("Instagram", 20)
    app3 = Aplicativo("Facebook", 30)
    app4 = Aplicativo("TikTok", 40)
    app5 = Aplicativo("YouTube", 50)

celular = Celular("Apple", "iPhone 14 Pro Max", 100)
celular.ligar()
celular.executar_app(celular.app1)
celular.executar_app(celular.app2)
celular.executar_app(celular.app3)
celular.executar_app(celular.app4)
celular.executar_app(celular.app5)

    
    