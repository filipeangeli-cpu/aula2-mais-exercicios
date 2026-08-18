class OrdemDeServico:
    total_os_criados = 0
    os_abertas = 0

    def __init__(self, cliente, descricao):
        self.descricao = descricao
        self.cliente = cliente
        OrdemDeServico.total_os_criados += 1
        OrdemDeServico.os_abertas += 1  

        self.status = "aberta"

    def finalizar_os(self):
        if self.status == "aberta":
            self.status = "finalizada"
            OrdemDeServico.os_abertas -= 1
            print(f"A ordem de serviço para {self.cliente} foi finalizada.")
        else:
            print("Todas as ordens de serviço já foram finalizadas.")

ordem1 = OrdemDeServico("João", "Conserto de computador")
ordem2 = OrdemDeServico("Maria", "Instalação de software")
ordem3 = OrdemDeServico("Pedro", "Manutenção de impressora")
ordem4 = OrdemDeServico("Ana", "Atualização de sistema")
ordem5 = OrdemDeServico("Carlos", "Formatação de notebook")

print(f"Total de ordens de serviço criadas: {OrdemDeServico.total_os_criados}")
print(f"Ordens de serviço abertas: {OrdemDeServico.os_abertas}")

ordem1.finalizar_os()
ordem2.finalizar_os()
ordem3.finalizar_os()
ordem3.finalizar_os() 