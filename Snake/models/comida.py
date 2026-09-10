import random
import pygame
from configures import ALTURA, LARGURA, TAMANHO_BLOCO, TELA, VERMELHO


class Comida:

    def __init__(self):
        self.posicao = self.gerar_posicao()

    def gerar_posicao(self, corpo_cobra=None):



        while True:
            coluna = random.randint(0, (LARGURA - TAMANHO_BLOCO) // TAMANHO_BLOCO)
            linha = random.randint(0, (ALTURA - TAMANHO_BLOCO) // TAMANHO_BLOCO)
            nova_posicao = [coluna * TAMANHO_BLOCO, linha * TAMANHO_BLOCO]


            if corpo_cobra is None or nova_posicao not in corpo_cobra:
                return nova_posicao

    def desenhar(self):
        pygame.draw.rect(
            TELA,
            VERMELHO,
            (self.posicao[0], self.posicao[1], TAMANHO_BLOCO, TAMANHO_BLOCO),
        )
