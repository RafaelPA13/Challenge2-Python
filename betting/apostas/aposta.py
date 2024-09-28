from models.equipe import Equipe
from models.piloto import Piloto
from partida import Podio

class Aposta:
    tipo: str
    pontos_ao_acertar: int
    def __init__(self, tipo: str, pontos_ao_acertar: int):
        self.tipo = tipo
        self.pontos_ao_acertar = pontos_ao_acertar

    # Verifica se o palpite do usuário está correto
    def obter_pontuacao(self, resultado: list[Podio]) -> int:
        pass

    # Coleta o palpite do usuário
    def coletar_aposta(self, pilotos: list[Piloto], equipes: list[Equipe]):
        pass

    # Exibe os palpites do usuário
    def exibir_palpites(self):
        pass

    # Exibe o resultado da aposta
    def exibir_resultado(self):
        pass
