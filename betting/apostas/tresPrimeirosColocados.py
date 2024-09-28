from betting.apostas.aposta import Aposta
from configs import CORES
from utils.terminal import escolher_opcao_index, printar_opcoes, exibir_com_cor
from models.equipe import Equipe
from models.piloto import Piloto
from partida import Podio


class ApostaTop3(Aposta):
    palpites: list[Piloto]
    podio: list[Podio]

    def __init__(self, pontos_ao_acertar: int):
        super().__init__('Top 3', pontos_ao_acertar)
        self.palpites = []

    def obter_pontuacao(self, resultado: list[Podio]):
        acertos = 0
        self.podio = resultado[:3]
        for i in range(3):
            if resultado[i].piloto == self.palpites[i]:
                acertos += self.pontos_ao_acertar
        return acertos

    def coletar_aposta(self, pilotos: list[Piloto], equipes: list[Equipe]):
        print("Faça sua aposta nos 3 primeiros colocados (digite o numero dos pilotos):")
        nomes_pilotos = list(map(lambda p: p.nome, pilotos))

        printar_opcoes(nomes_pilotos)
        for i in range(1, 4):
            piloto_index = escolher_opcao_index(f"{i}º colocado: ", nomes_pilotos)
            self.palpites.append(pilotos[piloto_index])
            print(f"{i}º colocado: {pilotos[piloto_index].nome}")

    def exibir_resultado(self):
        for i in range(3):
            exibir_com_cor(f"{i + 1}º colocado: {self.podio[i].piloto.nome} - seu palpite: {self.palpites[i].nome}",
                           CORES[self.palpites[i] == self.podio[i].piloto and "GREEN" or "RED"])

    def exibir_palpites(self):
        print("Top 3:")
        for i in range(3):
            print(f"{i + 1}º colocado: {self.palpites[i].nome}")
