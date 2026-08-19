class ItemBiblioteca:
    def __init__(self, titulo, codigo):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'O item "{self.titulo}" foi emprestado.')
        else:
            print(f'O item "{self.titulo}" não está disponível.')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'O item "{self.titulo}" foi devolvido.')
        else:
            print(f'O item "{self.titulo}" já está disponível.')


class Livro(ItemBiblioteca):
    def __init__(self, titulo, codigo, autor, num_paginas):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas

    def exibir_dados(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"Título: {self.titulo}")
        print(f"Código: {self.codigo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.num_paginas}")
        print(f"Status: {status}")


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item):
        if item.disponivel:
            item.emprestar()
            self.itens_emprestados.append(item)
            print(f'{self.nome} pegou "{item.titulo}".')
        else:
            print(f'{self.nome} não conseguiu pegar "{item.titulo}".')

    def devolver_item(self, item):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)
            print(f'{self.nome} devolveu "{item.titulo}".')
        else:
            print(f'{self.nome} não possui "{item.titulo}".')

    def ver_historico(self):
        print(f"\nItens com {self.nome}:")
        if not self.itens_emprestados:
            print("Nenhum item emprestado.")
        else:
            for item in self.itens_emprestados:
                print(f"- {item.titulo}")



livro1 = Livro("Dom Casmurro", 101, "Machado de Assis", 256)
livro2 = Livro("1984", 102, "George Orwell", 328)

usuario1 = Usuario("Filipe")


usuario1.pegar_item(livro1)
usuario1.pegar_item(livro2)


usuario1.ver_historico()

usuario1.pegar_item(livro1)

usuario1.devolver_item(livro1)

usuario1.ver_historico()