from betting.apostas.aposta import Aposta
from configs import CORES
from utils.terminal import escolher_opcao_index, printar_opcoes, exibir_com_cor
from models.equipe import Equipe
from models.piloto import Piloto
from partida import Podio


class ApostaMelhorVolta(Aposta):
    piloto: Piloto
    tempo_melhor_volta: float
    piloto_melhor_volta: Piloto

    def __init__(self):
        super().__init__('Melhor Volta')

    def avaliar(self, podios: list[Podio]):
        self.tempo_melhor_volta = podios[0].tempo_de_voltas[0]
        self.piloto_melhor_volta = podios[0].piloto

        for podio in podios:
            for tempo in podio.tempo_de_voltas:
                if tempo < self.tempo_melhor_volta:
                    self.tempo_melhor_volta = tempo
                    self.piloto_melhor_volta = podio.piloto
        return self.piloto.nome == self.piloto_melhor_volta.nome

    def coletar_aposta(self, pilotos: list[Piloto], equipes: list[Equipe]):
        print("\nAposte no piloto que fará a melhor volta:")
        nomes_pilotos = list(map(lambda p: p.nome, pilotos))
        printar_opcoes(nomes_pilotos)
        piloto_index = escolher_opcao_index(f"Numero do Piloto: ", nomes_pilotos)
        self.piloto = pilotos[piloto_index]

    def exibir_resultado(self):
        exibir_com_cor(f"Melhor Volta: {self.piloto_melhor_volta.nome} - {self.tempo_melhor_volta:.2f} segundos\n"
                       f"Piloto escolhido: {self.piloto.nome}",
                       CORES[self.piloto.nome == self.piloto_melhor_volta.nome and 'GREEN' or 'RED'])

    def exibir_palpites(self):
        print(f"Melhor Volta: {self.piloto.nome}")
