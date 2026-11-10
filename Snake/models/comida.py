
import random
import pygame

from configures import (
    ALTURA,
    LARGURA,
    TAMANHO_BLOCO,
    TELA,
    VERMELHO,
    VERMELHO_ESCURO,
)


class Comida:

    def __init__(self, limite_mapa=None, obstaculos=None):
        self.limite_mapa = limite_mapa
        self.obstaculos = obstaculos or []
        self.posicao = self.gerar_posicao()

    def gerar_posicao(self, corpo_cobra=None):
        colunas = LARGURA // TAMANHO_BLOCO
        linhas = ALTURA // TAMANHO_BLOCO

        posicoes_validas = []

        for coluna in range(colunas):
            for linha in range(linhas):
                x = coluna * TAMANHO_BLOCO
                y = linha * TAMANHO_BLOCO

                nova_posicao = [x, y]

                retangulo = pygame.Rect(
                    x,
                    y,
                    TAMANHO_BLOCO,
                    TAMANHO_BLOCO
                )

                # Não nascer sobre a cobrinha
                if corpo_cobra and nova_posicao in corpo_cobra:
                    continue

                # Não nascer fora dos limites do mapa
                if self.limite_mapa and not self.limite_mapa.contains(retangulo):
                    continue

                # Não nascer nos obstáculos
                if any(
                    retangulo.colliderect(obstaculo)
                    for obstaculo in self.obstaculos
                ):
                    continue

                posicoes_validas.append(nova_posicao)

        if not posicoes_validas:
            return None

        return random.choice(posicoes_validas)

    def desenhar(self):
        if self.posicao is None:
            return

        x, y = self.posicao

        retangulo = pygame.Rect(
            x,
            y,
            TAMANHO_BLOCO,
            TAMANHO_BLOCO
        )

        pygame.draw.rect(
            TELA,
            VERMELHO,
            retangulo,
            border_radius=5
        )

        pygame.draw.rect(
            TELA,
            VERMELHO_ESCURO,
            retangulo,
            width=2,
            border_radius=5
        )
