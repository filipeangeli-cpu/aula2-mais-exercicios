class Animal:
    def __init__(self, nome: str, especie: str, raca: str):
        self.nome = nome
        self.especie = especie
        self.raca = raca

    def fazer_som(self):
        print(f"o animal {self.nome} da espécie {self.especie} fez Barulho")

class Cachorro(Animal):
    def __init__(self, nome: str, especie: str, raca: str):
        super().__init__(nome, especie, raca)

    def fazer_som(self):
        print(f"o animal {self.nome} da espécie {self.especie} fez Barulho: AU!")

class Galinha(Animal):
    def __init__(self, nome: str, especie: str, raca: str):
        super().__init__(nome, especie, raca)

    def fazer_som(self):
        print(f"o animal {self.nome} da espécie {self.especie} fez Barulho: PÒÒÒÒÒÒÒÒÒÒÒÒÒ!")

class Vaca(Animal):
    def __init__(self, nome: str, especie: str, raca: str):
        super().__init__(nome, especie, raca)

    def fazer_som(self):
        print(f"o animal {self.nome} da espécie {self.especie} fez Barulho: MUUUUUUUUUUUUUUUUUUUU!")

cachorro = Cachorro("Chop", "Canino", "Vira-Lata")
galinha = Galinha("geralda", "ave", "galinha-caipira")
vaca = Vaca("bento", "bovino", "nelore")

cachorro.fazer_som()
galinha.fazer_som()
vaca.fazer_som()
