import os; os.system('clear')

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Salário: R$ {self.salario:.2f}")

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"Salário aumentado em {percentual}%!")


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario)
        self.setor = setor

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Setor: {self.setor}")

    def receber_bonificacao(self):
        bonus = self.salario * 0.10
        self.salario += bonus
        print("Parabéns! Você recebeu uma bonificação de 10%!")


# Testando o código
func = Funcionario("João", "123.456.789-00", 3000)
func.exibir_dados()
func.aumentar_salario(10)
func.exibir_dados()

print("\n--- GERENTE ---")

ger = Gerente("Maria", "987.654.321-00", 5000, "Financeiro")
ger.exibir_dados()
ger.aumentar_salario(5)
ger.receber_bonificacao()
ger.exibir_dados()