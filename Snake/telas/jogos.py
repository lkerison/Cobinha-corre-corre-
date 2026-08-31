import pygame
from configures import ALTURA, LARGURA, TAMANHO_BLOCO, TELA, VERDE


class Snake:

    def __init__(self):
        self.corpo = [
            [LARGURA // 2, ALTURA // 2],
            [LARGURA // 2 - TAMANHO_BLOCO, ALTURA // 2],
            [LARGURA // 2 - (TAMANHO_BLOCO * 2), ALTURA // 2],
        ]

        self.direcao = "RIGHT"
        self.nova_direcao = self.direcao
        self.crescer = False

    def mover(self):
        self.direcao = self.nova_direcao
        x, y = self.corpo[0]

        if self.direcao == "UP":
            y -= TAMANHO_BLOCO
        elif self.direcao == "DOWN":
            y += TAMANHO_BLOCO
        elif self.direcao == "LEFT":
            x -= TAMANHO_BLOCO
        elif self.direcao == "RIGHT":
            x += TAMANHO_BLOCO

        nova_cabeca = [x, y]
        self.corpo.insert(0, nova_cabeca)

        if not self.crescer:
            self.corpo.pop()
        else:
            self.crescer = False

    def desenhar(self):
        for i, segmento in enumerate(self.corpo):
            cor = VERDE if i == 0 else (0, 180, 0)

            pygame.draw.rect(
                TELA,
                cor,
                (segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO),
            )

    def verificar_colisao(self):
        x, y = self.corpo[0]

        # Colisão com as bordas da tela
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            return True

        # Colisão com o próprio corpo
        if self.corpo[0] in self.corpo[1:]:
            return True

        return False
