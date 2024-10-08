from betting.apostas.aposta import Aposta
from configs import CORES
from utils.terminal import exibir_com_cor, printar_cabecalho, limpar_terminal
from models.equipe import Equipe
from models.piloto import Piloto
from partida import Podio


class BettingSystem:
    def __init__(self, apostas: list[Aposta], pilotos: list[Piloto], equipes: list[Equipe]):
        self.pilotos = pilotos
        self.equipes = equipes
        self.apostas = apostas

    def coletar_apostas(self):
        for aposta in self.apostas:
            aposta.coletar_aposta(self.pilotos, self.equipes)

        limpar_terminal()
        printar_cabecalho("Suas apostas")
        for aposta in self.apostas:
            aposta.exibir_palpites()

    def avaliar_apostas(self, resultados_podio: list[Podio]):
        printar_cabecalho("Resultado das Apostas")
        pontos_total = 0
        for aposta in self.apostas:
            print(f"Resultado: {aposta.tipo}\n")
            pontos = aposta.obter_pontuacao(resultados_podio)
            pontos_total += pontos
            aposta.exibir_resultado()
            if pontos > 0:
                exibir_com_cor(
                    f"Deu green! Você fez {pontos} pontos com essa aposta, atingindo um total de {pontos_total} pontos!",
                    CORES['GREEN'])
            else:
                exibir_com_cor("Poxa! Você não pontuou :(", CORES['RED'])
            print("-" * 50)

        print(f"Pontuação total: {pontos_total}")
