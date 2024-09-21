from models.equipe import Equipe
from models.piloto import Piloto
from partida import Podio

class Aposta:
    def __init__(self, tipo):
        self.tipo = tipo

    def avaliar(self, resultado: list[Podio]):
        pass

    def coletar_aposta(self, pilotos: list[Piloto], equipes: list[Equipe]):
        pass

    def exibir_palpites(self):
        pass

    def exibir_resultado(self):
        pass
