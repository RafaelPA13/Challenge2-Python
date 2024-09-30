from models.equipe import Equipe

class Piloto:
    nome: str
    equipe: Equipe
    cor: str

    def __init__(self, nome, equipe, cor):
        self.nome = nome
        self.equipe = equipe
        self.cor = cor

    def __str__(self):
        return f"{self.nome} - {self.equipe.nome}"