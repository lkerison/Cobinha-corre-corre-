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

    def __init__(self):
        self.posicao = self.gerar_posicao()

    def gerar_posicao(self, corpo_cobra=None):
        """Gera coordenadas na grade garantindo que a comida não apareça sobre a cobra."""
        colunas = LARGURA // TAMANHO_BLOCO
        linhas = ALTURA // TAMANHO_BLOCO

        while True:
            x = random.randint(0, colunas - 1) * TAMANHO_BLOCO
            y = random.randint(0, linhas - 1) * TAMANHO_BLOCO
            nova_posicao = [x, y]

            if corpo_cobra is None or nova_posicao not in corpo_cobra:
                return nova_posicao

    def desenhar(self):
        x, y = self.posicao[0], self.posicao[1]
        retangulo = pygame.Rect(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)


        pygame.draw.rect(TELA, VERMELHO, retangulo, border_radius=5)
        pygame.draw.rect(
            TELA, VERMELHO_ESCURO, retangulo, width=2, border_radius=5
        )
