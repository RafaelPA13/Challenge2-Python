import random
import time

from utils.terminal import limpar_terminal, exibir_com_cor
from models.piloto import Piloto


class PilotoState:
    completou_a_corrida: bool = False
    entrou_no_podio: bool = False
    piloto: Piloto
    posicao_pista: int
    espacamento_do_nome: int
    destino: int
    volta_atual: int
    tempos_das_voltas: list[float]
    inicio_da_volta: float = None
    posicao_podio: int = 0

    def __init__(self, piloto, posicao, espacamento_do_nome, destino=100, numero_de_voltas=3):
        self.piloto = piloto
        self.posicao_pista = posicao
        self.espacamento_do_nome = espacamento_do_nome
        self.destino = destino
        self.volta_atual = 1
        self.numero_de_voltas = numero_de_voltas
        self.tempos_das_voltas = []
        self.inicio_da_volta = None

    def acelerar(self):
        if self.completou_a_corrida:
            return
        if self.posicao_pista == 0:
            self.inicio_da_volta = time.time()

        # clamp para evitar que a posição ultrapasse o destino
        self.posicao_pista = min(self.posicao_pista + random.randint(1, 3), self.destino)

        # Conclui a volta atual
        if self.posicao_pista >= self.destino:
            self.completar_volta()

    def completar_volta(self):
        tempo_da_volta = time.time() - self.inicio_da_volta
        self.tempos_das_voltas.append(tempo_da_volta)
        self.volta_atual += 1
        if self.volta_atual > self.numero_de_voltas:
            self.completou_a_corrida = True
            self.volta_atual = self.numero_de_voltas
        else:
            self.posicao_pista = 0

    def mostrar_corrida(self):
        nome = self.piloto.nome + " " * self.espacamento_do_nome
        exibir_com_cor(
            f"{nome}: {'-' * self.posicao_pista}🚘{'-' * (self.destino - self.posicao_pista)}🏁 (Volta {self.volta_atual})",
            self.piloto.cor)

    def finalizou_a_corrida(self):
        return self.completou_a_corrida

    def mostrar_leaderboard(self, posicao_geral):
        cabecalho = f"{posicao_geral} - {self.piloto.nome}"
        if self.completou_a_corrida:
            cabecalho += f" - 🏁 {sum(self.tempos_das_voltas):.2f} segundos"
        print(cabecalho)
        for i, tempo in enumerate(self.tempos_das_voltas):
            print(f"    Volta {i + 1}: {tempo:.2f} segundos")


class Podio:
    tempo_de_voltas: list[float]
    tempo_total_segundos: float
    piloto: Piloto
    posicao: int

    def __init__(self, piloto, posicao, tempo_de_voltas):
        self.piloto = piloto
        self.posicao = posicao
        self.tempo_de_voltas = tempo_de_voltas
        self.tempo_total_segundos = sum(tempo_de_voltas)


class Game:
    podio_pilotos = list[Podio]
    pilotos: list[PilotoState]
    pilotos_participantes: list[Piloto]

    def __init__(self, pilotos, equipes, velocidade=0.5, numero_de_voltas=3):
        self.pilotos_participantes = pilotos
        self.equipes = equipes
        self.velocidade_da_corrida = velocidade
        self.numero_de_voltas = numero_de_voltas

    def iniciar_corrida(self):
        self.pilotos = []
        self.podio_pilotos = []
        tamanho_do_maior_nome = max([len(piloto.nome) for piloto in self.pilotos_participantes])

        for piloto in self.pilotos_participantes:
            espacamento = tamanho_do_maior_nome - len(piloto.nome) + 3  # Usado para alinhar as pistas
            self.pilotos.append(PilotoState(piloto, 0, espacamento, 100, self.numero_de_voltas))

        while len(self.podio_pilotos) < len(self.pilotos):
            limpar_terminal()
            self.atualizar_corrida()
            self.exibir_leaderboard()
            time.sleep(0.5 * self.velocidade_da_corrida)

        limpar_terminal()
        return self.podio_pilotos

    def atualizar_corrida(self):
        for piloto in self.pilotos:
            piloto.acelerar()
            piloto.mostrar_corrida()

            if piloto.completou_a_corrida and not piloto.entrou_no_podio:
                podio = Podio(piloto.piloto, len(self.podio_pilotos) + 1, piloto.tempos_das_voltas)
                piloto.entrou_no_podio = True
                piloto.posicao_podio = len(self.podio_pilotos) + 1
                self.podio_pilotos.append(podio)

    def exibir_leaderboard(self):
        pilotos = sorted(self.pilotos,
                         key=lambda piloto: (
                             len(self.podio_pilotos) - piloto.posicao_podio, piloto.volta_atual * piloto.posicao_pista),
                         reverse=True)
        for i, piloto in enumerate(pilotos):
            piloto.mostrar_leaderboard(i + 1)
            print()
