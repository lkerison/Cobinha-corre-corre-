import pygame
import random

from configures import (
    TELA,
    LARGURA,
    ALTURA,
    TAMANHO_BLOCO,
    VERMELHO
)

class Comida:
    def __init__(self):
        self.posicao = self.gerar_posicao()

    def gerar_posicao(self):
        x = random.randint(0, (LARGURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO
        y = random.randint(0, (ALTURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO
        return [x, y]

    def desenhar(self):
        pygame.draw.rect(
            TELA,
            VERMELHO,
            (self.posicao[0], self.posicao[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        )