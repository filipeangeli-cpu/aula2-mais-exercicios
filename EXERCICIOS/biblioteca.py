class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas}"

    def comparar_paginas(self, outro_livro):
        if self.paginas > outro_livro.paginas:
            return f"{self.titulo} tem mais páginas que {outro_livro.titulo}"
        elif self.paginas < outro_livro.paginas:
            return f"{self.titulo} tem menos páginas que {outro_livro.titulo}"
        else:
            return f"{self.titulo} e {outro_livro.titulo} têm o mesmo número de páginas"
        

    def diferenca_paginas(self, outro_livro):
        return abs(self.paginas - outro_livro.paginas)

livro = Livro("como parar de ser trouxa", "Caio Carneiro", 200)
livro2 = Livro("O Guia Pratico Para Se Valorizar nas relações", "Mary Spin", 129)
print(livro)
print(livro2)
print(livro.comparar_paginas(livro2))
print(f"Diferença de páginas: {livro.diferenca_paginas(livro2)}")