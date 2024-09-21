from betting.apostas.aposta import Aposta
from configs import CORES
from utils.terminal import escolher_opcao_index, printar_opcoes, exibir_com_cor
from models.equipe import Equipe
from models.piloto import Piloto
from partida import Podio


class ApostaMelhorEquipe(Aposta):
    equipe: Equipe
    equipe_vencedora: str

    def __init__(self):
        super().__init__('Melhor Equipe')

    def avaliar(self, resultados: list[Podio]):
        pontos_por_posicao = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
        pontos_por_equipe = {}
        for podio in resultados:
            equipe_nome = podio.piloto.equipe.nome
            pontos = pontos_por_posicao.get(podio.posicao, 0)
            pontos_por_equipe[equipe_nome] = pontos_por_equipe.get(equipe_nome, 0) + pontos

        self.equipe_vencedora = max(pontos_por_equipe, key=pontos_por_equipe.get)
        return self.equipe.nome == self.equipe_vencedora

    def exibir_resultado(self):
        exibir_com_cor(f"Melhor Equipe: {self.equipe_vencedora}\n"
                       f"Equipe escolhida: {self.equipe.nome}",
                       CORES[self.equipe.nome == self.equipe_vencedora and 'GREEN' or 'RED'])

    def coletar_aposta(self, pilotos: list[Piloto], equipes: list[Equipe]):
        print("\nAposte na equipe que fará mais pontos:")
        nome_equipes = list(map(lambda e: e.nome, equipes))
        printar_opcoes(nome_equipes)

        melhor_equipe_index = escolher_opcao_index("Digite o número da equipe: ", nome_equipes)
        self.equipe = equipes[melhor_equipe_index]

    def exibir_palpites(self):
        print(f"Melhor Equipe: {self.equipe.nome}")
