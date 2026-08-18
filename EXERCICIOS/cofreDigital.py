class CofreDigital:
    def __init__(self, titular: str, senha: str):
        if not isinstance(senha, str) or len(senha) != 4 or not senha.isdigit():
            raise ValueError("Senha deve ser uma string de 4 dígitos.")
        self.titular = titular
        self.__senha = senha       
        self.__saldo = 0.0       

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo.")
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}")

    def sacar(self, valor: float, senha_informada: str):
        if senha_informada != self.__senha:
            print("Senha incorreta! Acesso negado.")
            return False
        if valor <= 0:
            print("Valor de saque inválido.")
            return False
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    
    def obter_saldo(self, senha_informada: str):
        if senha_informada != self.__senha:
            print("Senha incorreta! Acesso negado.")
            return None
        return self.__saldo


if __name__ == "__main__":
    
    cofre = CofreDigital("Filipe", "1307")

    # Deposita e tenta sacar
    cofre.depositar(100.0)                       
    cofre.sacar(30.0, "0000")                  
    cofre.sacar(30.0, "1234")                    

    
   
    cofre.__saldo = 1_000_000.0
    cofre.__senha = "0000"

    print("\nTentativa de alteração direta feita: atribuindo cofre.__saldo e cofre.__senha")
    print("Atributos do objeto (conta.__dict__):")
    for k, v in cofre.__dict__.items():
        print(f"  {k!r}: {v!r}")

   
    
    print("\nTentando sacar R$10,00 com a senha original '1234' após a tentativa de alteração direta:")
    cofre.sacar(10.0, "1234")  
  
   